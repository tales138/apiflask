import pytest
from app.server import app  
from app.server import db  # Certifique-se de que este seja o ORM correto configurado
from app.models.usuario import Usuario  # O modelo de usuário do banco

@pytest.fixture(autouse=True)
def clear_database():
    """Limpa o banco de dados antes de cada teste."""
    with app.app_context():
        #db.session.query(Usuario).delete()
        db.session.commit()
        db.session.rollback()
@pytest.fixture(scope="module")
def client():
    """Cria um cliente de teste com contexto de aplicação."""
    with app.app_context():
        yield app.test_client()

@pytest.fixture
def usuario_existente():
    """Adiciona um usuário existente ao banco de dados para testes."""
    with app.app_context():
        usuario = Usuario(name="Usuário Teste", email="tese@example.com", password="senha123")
        db.session.add(usuario)
        db.session.commit()
        db.session.rollback()
        return usuario

def test_cadastrar_usuario_sucesso(client):
    """Testa o cenário de sucesso ao cadastrar um usuário."""
    payload = {
        "name": "João Silva",
        "email": "joao.si@exl.com",
        "password": "Son@qwe1234"
    }
    response = client.post("/cadastrar", json=payload)

    assert response.status_code == 201
    assert response.json == {"Success": "Usuario cadastrado com suscesso"}

def test_cadastrar_usuario_json_invalido(client):
    """Testa o cenário onde o payload enviado não é um JSON válido."""
    response = client.post("/cadastrar", data="não é um JSON válido", content_type="application/json")

    assert response.status_code == 400
    assert response.json == {"Error": "Campos obrigatórios ausentes ou inválidos"}
