from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# Codifica la contraseña
password = "mpdb1985*"
encoded_password = quote_plus(password)

# Cadena de conexión
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://distrib3_user:{encoded_password}@distribuidoravega.cl:3306/distrib3_app"

# Crea el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configura la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()