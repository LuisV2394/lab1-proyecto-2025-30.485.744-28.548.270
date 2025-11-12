import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True
 
#Prueba para verificar que las variables se cargan correctamente    
#config = Config()
#print("Database URL:", config.SQLALCHEMY_DATABASE_URI)
#print("JWT Secret Key:", config.JWT_SECRET_KEY)