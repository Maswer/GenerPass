import secrets

def create_new(length, characters):
    """Функция генераций пароля"""
    return "".join(secrets.choice(characters) for _ in range(length))