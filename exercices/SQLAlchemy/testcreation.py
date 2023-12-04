from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

# Création de la base de données
Base = declarative_base()

# Déclaration du moteur de base de données
engine = create_engine('sqlite:///tmpdb.sqlite', echo=True)
from sqlalchemy_utils import database_exists, drop_database, create_database

if database_exists(engine.url):
    drop_database(engine.url)    

create_database(engine.url)

if database_exists(engine.url):
    print(f"La base de données '{engine.url}' existe.")
else:
    print(f"La base de données '{engine.url}' n'existe pas.")

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Créez une session
Session = sessionmaker(bind=engine)
session = Session()

# Créez une base déclarative
Base = declarative_base()

# Définissez la classe Product pour la table "products"
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    price = Column(Float)

# Définissez la classe Customer pour la table "customers"
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255))

# Définissez la classe Order pour la table "orders"
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    products = relationship("Product")
    customers = relationship("Customer")

#, back_populates="orders"

# Utilisez la méthode create_all() pour créer les tables
Base.metadata.create_all(engine)

# Créez les objets Product avec les données à insérer

productstest = [
    {"id": 1, "name": "Produit_1", "price": 100},
    {"id": 2, "name": "Produit_2", "price": 200},
]

customerstest = [
    {"id": 1, "name": "user_1", "email": "u1@u.fr"},
    {"id": 2, "name": "user_2", "email": "u2@u.fr"},
]

orderstest = [
    {"id": 1, "customer_id": 1, "product_id": 1},
    {"id": 2, "customer_id": 2, "product_id": 2},
]

# Ajoutez les objets à la session et commettez les changements

user_objects1 = [Product(**product) for product in productstest]
session.add_all(user_objects1)

user_objects2 = [Customer(**customer) for customer in customerstest]
session.add_all(user_objects2)

user_objects3 = [Order(**order) for order in orderstest]
session.add_all(user_objects3)

session.commit()

# Fermez la session

query1 = session.query(Product)
query2 = session.query(Customer)
query3 = session.query(Order)

# Utilisez la méthode all() pour récupérer tous les résultats de la requête
productsquery = query1.all()
customerquery = query2.all()
orderquery = query3.all()


# Affiche les éléments de la table produits, customers et orders
for product in productsquery:
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")
# Affichez les résultats
for customer in customerquery:
    print(f"ID: {customer.id}, Name: {customer.name}, email: {customer.email}")
# Affichez les résultats
for order in orderquery:
    print(f"ID: {order.id}, customer_id: {order.customer_id}, product_id: {order.product_id}")

# Affiche les éléments de la table produits, customers et orders avec join

query = session.query(Order.id, Product.name, Product.price, Customer.name, Customer.email)

query1 = query.join(Product, Product.id ==  Order.product_id)
query2 = query1.join(Customer, Customer.id ==  Order.customer_id)

queryall = query2.all()

for querytest in queryall:
    print(f"{querytest}")

# changer prix du produit 2

queryproduct2 = session.get(Product, 2)

nouveauprix = 500
queryproduct2.price = nouveauprix

session.commit()

####

query = session.query(Order.id, Product.name, Product.price, Customer.name, Customer.email)

query1 = query.join(Product, Product.id ==  Order.product_id)
query2 = query1.join(Customer, Customer.id ==  Order.customer_id)

queryall = query2.all()

for querytest in queryall:
    print(f"{querytest}")

### Supprimer Order id 2

order2delete = session.query(Order).filter(Order.id == 2)
order2delete.delete()

session.commit()

####

query = session.query(Order.id, Product.name, Product.price, Customer.name, Customer.email)

query1 = query.join(Product, Product.id ==  Order.product_id)
query2 = query1.join(Customer, Customer.id ==  Order.customer_id)

queryall = query2.all()

for querytest in queryall:
    print(f"{querytest}")

session.close()