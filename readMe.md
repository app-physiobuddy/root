# Inicializar a aplicação

Esta é a pasta root, todos os outros repositórios devem ser colonados como filhos desta pasta.

- 1. Fazer as .env de acordo com o .env_example

Depois, para o broker (EMQX mqtt) funcionar, é necessário:
- 1. Abrir o dashboard com user:admin e pass:password
- 2. Criar utilizador de autenticação com todos os passos _default_ e com user e password (superuser=false) que depois serão também colocados no node-red (notifications service)


>IMPORTANTE: Por vezes o exercise server e o entities server iniciam antes da base de dados estar pronta e a inicialização da base de dados falha. Por garantias, restart os dois containers
```docker restart exercise_server entities_server```

Na coleção do postman tem a flow do processo de negócio da app.
As bases de dados estão vazias, pelo que deverá ser possivel correr cada um dos endpoints da coleção sem fazer nenhuma alteração. 
Adicionalmente, esta coleção do postman está pronta para correr automáticamente (_run collection_) e testar todos os endpoints rapidamente.



### Architecture (second iteration)

Most recent updates are in red color. The project's architecture was reviewed to resolve problems and make improvements, culminating in:
- adding caching (redis) to the Coordination services. This was only implemented in coordination service B, in the therapistGetsAllExercisesWithCompanyUserId controller.
- upload service added and implemented, integrated with _message broker_
    - Interoperability with third-party apps: it's the same idea, so I didn't implement it
- tsl secure communication (not implemented in dev)


<img src="https://drive.usercontent.google.com/download?id=1MGUxqFsmQbl4iMZhmjhtudlh6Ai92L-Q&export=view" width="600"/>

# Initialize the application


This is the root folder, all other repositories must be coloned as children of this folder.

- 1. make the .env according to the .env_example

Next, for the broker (EMQX mqtt) to work, you need to:
- 1. open the dashboard with user:admin and pass:password
- 2. create an authentication user with all the _default_ steps and with a user and password (superuser=false) which will then also be placed in the node-red (notifications service)


>IMPORTANT: Sometimes the exercise server and the entities server start before the database is ready and the database initialization fails. For guarantees, restart both containers
```docker restart exercise_server entities_server```

In the postman collection you have the flow of the app's business process.
The databases are empty, so it should be possible to run each of the endpoints in the collection without making any changes. 
In addition, this postman collection is ready to run automatically (_run collection_) and test all the endpoints quickly.

