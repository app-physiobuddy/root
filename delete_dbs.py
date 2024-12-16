import subprocess
import os

port_mapping = {
    "auth_db": 5001,
    "exercise_db": 5002,
    "entities_db": 5004,
}


def manage_containers(containers_info, network_name, volumes_prefix="physio_buddy_"):
    for container_name, image_name in containers_info:

        # Load environment file for the container if it exists
        env_file = f".env_{container_name}"
        env_args = ["--env-file", env_file] if os.path.exists(env_file) else []
        pg_port = port_mapping[container_name]
        print(f"Using PG_PORT: {pg_port}")

        # Stop and remove container
        print(f"Stopping and removing container: {container_name}")
        subprocess.run(["docker", "stop", container_name], check=False)
        subprocess.run(["docker", "rm", container_name], check=False)

        # Remove old volume
        volume_name = f"{volumes_prefix}{container_name}"
        print(f"Removing volume: {volume_name}")
        subprocess.run(["docker", "volume", "rm", volume_name], check=False)

        # Create new volume
        print(f"Creating volume: {volume_name}")
        subprocess.run(["docker", "volume", "create", volume_name], check=True)

        # Run newer containers of dbs
        print(f"Running container: {container_name} with image: {image_name}")
        run_command = (
            [
                "docker",
                "run",
                "-d",
                "--name",
                container_name,
                "--network",
                network_name,
                "-v",
                f"{volume_name}:/data",
                "-p",
                f"{pg_port}:{pg_port}",
            ]
            + env_args
            + [image_name]
        )

        try:
            subprocess.run(run_command, check=True)
            print(f"Container {container_name} started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to start container {container_name}. Error: {e}")

    subprocess.run(["sleep", "1"])

    subprocess.run(["docker", "restart", "exercise_server", "entities_server"])


def main():
    containers = [
        ("entities_db", "physio_buddy-entities_db"),
        ("exercise_db", "physio_buddy-exercise_db"),
        ("auth_db", "physio_buddy-auth_db"),
    ]

    volumes_prefix = "physio_buddy_"
    network_name = f"{volumes_prefix}physiobuddy-network"

    manage_containers(containers, network_name, volumes_prefix)


if __name__ == "__main__":
    main()
