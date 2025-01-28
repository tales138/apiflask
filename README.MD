# API Flask com Docker

Esta API foi desenvolvida para gerenciar usuários, incluindo autenticação e permissões administrativas, utilizando Flask e PostgreSQL. A aplicação está containerizada com Docker.

---

## Rotas da API

### Rotas de Usuários
- **[POST] /cadastrar**  
  Cadastrar um novo usuário.  
  *Essa rota serve para cadastrar um novo usuário.*

- **[DELETE] /usuario/{id}**  
  Excluir um usuário.  
  *Essa rota serve para excluir um usuário.*

- **[GET] /usuários**  
  Retorna a lista de usuários cadastrados. *(Permitido apenas para admins)*  
  *Essa rota serve para retornar uma lista de usuários cadastrados.*

- **[PUT] /usuarios/{id}**  
  Atualizar dados de um usuário existente.  
  *Essa rota atualiza os dados de um usuário.*

---

### Rotas de Autenticação
- **[POST] /login**  
  Login de usuário (retorna o token JWT e o ID do usuário).  
  *Rota usada para autenticar usuários.*

- **[POST] /logout**  
  Logout de usuário.  
  *Rota usada para fazer o logout de usuários.*

- **[POST] /refereshtoken**  
  Renovar o token de autenticação.  
  *Se o token expirou, retorna um novo. Caso contrário, retorna o mesmo token.*

---

### Rotas de Administração
- **[POST] /promoteadmin**  
  Promover usuário a administrador. *(Apenas admins podem usar esta rota)*  
  *Esta rota deve ser usada para cadastrar novos administradores.*

- **[POST] /promoteadmintest**  
  Promover usuário a administrador (para fins de teste).  
  *No caso de o banco de dados estar vazio, permite que qualquer usuário logado promova outro a admin para testar as permissões.*

---
Para que o usuário possa ter uma visualização gráfica do banco de dados foi usado o container docker adminer como dependência da aplicação, podendo ser acessado em:
```
http://127.0.0.1:8080/
```

As rotas da aplicação seguiram o padrão REST.

Para realizar a autenticação foi utilizado o mecanismo de token JWT.

Para a documentação e teste da API, foi utilizado o Swagger de forma incorporada a api.

Essa documentação pode ser acessada quando a aplicação for iniciada. em:
```
http://127.0.0.1:5000/apidocs 
```

Testes Unitários:
Para a realização de testes unitários foi utilizado a biblioteca Pytest
Os arquivos de teste estão na pasta /app/tests e podem ser executados com seguinte comando:
```
pytest -v app/tests/nome_do_arquivo.py
```
Os testes não foram executados usando docker. Então, para executá-los, é necessário executar a aplicação seguindo os passos de inicialização sem docker.


##Execução Sem Docker:

Abra o arquivo db_connection.py no diretório app/extensions e descomente a seguinte linha de código
```
#app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:12345@localhost:5432/postgres"
```
Você pode editar os parâmetros de conexão com o postgre de acordo com as configurações do seu banco local.

Tenha o postgresql instalado na sua máquina e use o Dbeaver para ter uma visualização gráfica do banco de dados.

comente a seguinte linha de código:
```
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
```

no diretório do repositório clonado:

execute:

para instalar as dependências da aplicação
```
pip install requirements.txt
```
para iniciar a aplicação:
```
flask --app run run 
```

Execução com Docker: 

execute o comando para listar os containers ativos: 
```
docker ps -a
```
no diretório raiz do projeto execute o seguinte comando para gerar o container docker da aplicação juntamente com o banco de dados e visualizador gráfico adminer :
```
docker compose build 
```
Para executar o container:
```
docker compose up api_flask
```
