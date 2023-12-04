from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

# Création de la base de données
Base = declarative_base()

# Déclaration de la table `users`
class User(Base):
	__tablename__ = "user"
id = Column(Integer, primary_key=True)
name = Column(String(255))

# Déclaration du moteur de base de données
engine = create_engine('sqlite:///database.sqlite')

# Création de la base de données
Base.metadata.create_all(engine)