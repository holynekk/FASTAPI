from passlib.context import CryptContext

# Sayin which crypt algo we will use
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

