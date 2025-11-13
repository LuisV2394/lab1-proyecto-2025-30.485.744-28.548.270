from passlib.hash import bcrypt

# La contraseña que quieres hashear
password = "Secret123"

# Generar el hash
hashed = bcrypt.hash(password)

print("Password:", password)
print("Hashed:", hashed)
