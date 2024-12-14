# Inicializar a aplicação

Esta é a pasta root, todos os outros repositórios devem ser colonados como filhos desta pasta.

- 1. Fazer as .env de acordo com o .env_example

Depois, para o broker funcionar, é necessário:
- 1. Abrir o dashboard com user:admin e pass:password
- 2. Criar utilizador de autenticação com todos os passos _default_ e com user e password (superuser=false) que depois serão também colocados no node-red (notifications service)


>IMPORTANTE: Por vezes o exercise server e o entities server iniciam antes da base de dados estar pronta e a inicialização da base de dados falha. Por garantias, restart os dois containers
```docker restart exercise_server entities_server```

Na coleção do postman tem a flow do processo de negócio da app.
As bases de dados estão vazias, pelo que deverá ser possivel correr cada um dos endpoints da coleção sem fazer nenhuma alteração. 
Adicionalmente, esta coleção do postman está pronta para correr automáticamente (_run collection_) e testar todos os endpoints rapidamente.

