import re

def is_valid_email(email):
    # Regex para verificar formato de email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Validar email com regex
    if re.match(email_regex, email):
        return True
    return False

def is_valid_name(name):
    # Regex para validar o nome
    name_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$"
    
    # Verificar se o nome corresponde ao padrão
    if re.match(name_regex, name) and len(name.strip()) > 1:
        return True
    return False



def is_password_strong(password):
    """
    Verifica se a senha é forte com base nos seguintes critérios:
    - Pelo menos 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    - Pelo menos 1 caractere especial
    
    Args:
        password (str): A senha a ser verificada.

    Returns:
        bool: True se a senha for forte, False caso contrário.
    """
    if len(password) < 8:
        return False

    # Verifica pelo menos uma letra maiúscula
    if not re.search(r"[A-Z]", password):
        return False

    # Verifica pelo menos uma letra minúscula
    if not re.search(r"[a-z]", password):
        return False

    # Verifica pelo menos um número
    if not re.search(r"[0-9]", password):
        return False

    # Verifica pelo menos um caractere especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True