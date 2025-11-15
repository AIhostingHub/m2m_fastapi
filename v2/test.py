
from passlib.context import CryptContext
pwd = "adminpass"  # <-- replace with your real password
ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(ctx.hash(pwd))
