from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.settings import settings

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    try:
        ph.verify(password_hash, password)
        return True
    except VerifyMismatchError:
        return False


def create_access_token(subject: str) -> tuple[str, int]:
    expire = datetime.now(timezone.utc) + timedelta(hours=settings.JWT_EXPIRE_HOURS)
    payload = {"sub": subject, "exp": expire}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)
    expires_in = int((expire - datetime.now(timezone.utc)).total_seconds())
    return token, expires_in

def decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
        sub = payload.get("sub")
        if not sub:
            raise ValueError("Missing subject")
        return sub
    except (JWTError, ValueError) as e:
        raise ValueError("Invalid token") from e
