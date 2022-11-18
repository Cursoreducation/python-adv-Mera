from uuid import uuid4


def generate_password_reset_id() -> str:
    return str(uuid4())
