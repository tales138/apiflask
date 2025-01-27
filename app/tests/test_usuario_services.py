import pytest
import uuid
from app.services.usuario_services.usuarios_services import (
    user_create, user_delete, is_user_valid,
    get_user_id, get_all_users, check_password,
    edit_user, delete_user
)
from app.server import app  # Certifique-se de que você tem uma factory para criar a aplicação
from app.server import db  # Extensão do banco de dados
from app.models.usuario import Usuario  # Importando o modelo de Usuario

# Fixture para limpar o banco de dados antes de cada teste
@pytest.fixture(autouse=True)
def clear_database():
    """Limpa o banco de dados antes de cada teste."""
    with app.app_context():
        db.session.query(Usuario).delete()
        db.session.commit()
        db.session.rollback()
        #db.session.remove()  # Garante que qualquer transação anterior seja limpa

# Fixture para gerar dados únicos de usuário
@pytest.fixture
def unique_user_data():
    """Gera dados únicos para um usuário."""
    return {
        "name": "Test User",
        "email": f"testuser_{uuid.uuid4().hex[:8]}@example.com",  # Email único com UUID
        "password": "StrongP@ssw0rd!"
    }

# Fixture para o cliente de testes (com contexto de aplicação)
@pytest.fixture(scope="module")
def test_client():
    """Cria um cliente de teste com contexto de aplicação."""
    with app.app_context():
        yield app.test_client()

# Testes com Pytest

def test_user_creation_valid(test_client, unique_user_data):
    """Testa a criação de um usuário válido."""
    result = user_create(**unique_user_data)
    assert result, "O usuário deveria ser criado com sucesso."

    user = Usuario.query.filter_by(email=unique_user_data["email"]).first()
    assert user is not None, "O usuário não foi encontrado no banco de dados."
    assert user.name == unique_user_data["name"], "O nome do usuário está incorreto."

def test_user_creation_invalid_email(test_client):
    """Testa a criação de um usuário com email inválido."""
    invalid_user_data = {
        "name": "Invalid User",
        "email": "invalid-email",
        "password": "StrongP@ssw0rd!"
    }
    result = user_create(invalid_user_data["name"], invalid_user_data["email"], invalid_user_data["password"])
    assert not result, "O usuário não deveria ser criado com email inválido."

def test_user_creation_invalid_password(test_client, unique_user_data):
    """Testa a criação de um usuário com senha fraca."""
    result = user_create(unique_user_data["name"], unique_user_data["email"], "weak")
    assert not result, "O usuário não deveria ser criado com senha fraca."

def test_user_deletion(test_client, unique_user_data):
    """Testa a exclusão de um usuário."""
    # Primeiro, cria o usuário
    user_create(**unique_user_data)
    user = Usuario.query.filter_by(email=unique_user_data["email"]).first()
    
    # Realiza a exclusão
    user_delete(user.id)

    # Reverificar se o usuário foi realmente deletado
    user = Usuario.query.filter_by(email=unique_user_data["email"]).first()
    assert user is None, "O usuário deveria ser deletado do banco de dados."

def test_check_password(test_client, unique_user_data):
    """Testa a verificação de senha."""
    # Primeiro, cria o usuário
    user_create(**unique_user_data)
    user = Usuario.query.filter_by(email=unique_user_data["email"]).first()
    
    result = check_password(user.email, unique_user_data["password"])
    assert result, "A verificação de senha deveria retornar True."

    result = check_password(user.email, "WrongPassword")
    assert not result, "A verificação de senha deveria retornar False."

def test_edit_user(test_client, unique_user_data):
    """Testa a edição de um usuário."""
    # Primeiro, cria o usuário
    user_create(**unique_user_data)
    user = Usuario.query.filter_by(email=unique_user_data["email"]).first()
    
    new_name = "Jane Doe"
    new_email = "janedoe@example.com"
    edit_user(user.id, new_name, new_email)

    user = Usuario.query.filter_by(id=user.id).first()
    assert user.name == new_name, "O nome do usuário não foi atualizado."
    assert user.email == new_email, "O email do usuário não foi atualizado."

def test_get_all_users(test_client, unique_user_data):
    """Testa a obtenção de todos os usuários."""
    # Primeiro, cria o usuário
    user_create(**unique_user_data)
    
    users = get_all_users()
    assert len(users) >= 1, "Deveria haver pelo menos um usuário."
    assert any(user['email'] == unique_user_data["email"] for user in users), "O usuário deveria estar na lista."
