
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///shop.db")

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def add_product(name, price, stock):
    session = Session()

    product = Product(
        name=name,
        price=price,
        stock=stock
    )

    session.add(product)
    session.commit()
    session.close()


def get_all_products():
    session = Session()

    products = session.query(Product).all()

    result = []

    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        })

    session.close()

    return result


def delete_product(product_id):
    session = Session()

    product = session.query(Product).filter(
        Product.id == product_id
    ).first()

    if product:
        session.delete(product)
        session.commit()

    session.close()
