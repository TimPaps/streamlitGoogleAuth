import secrets

# Générer une clé secrète sécurisée
cookie_secret = secrets.token_hex(32)
print("Votre cookie secret : ", cookie_secret)