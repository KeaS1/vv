from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Customers(Base):
    __tablename__ = "customers"
    customers_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    phone_id: Mapped["Phone"] = relationship(back_populates="customers")
    addresses: Mapped[str] = mapped_column(String(64))
    def __repr__(self) -> str:
        return f"Customers(customers_id={self.customers_id!r}, first_name={self.first_name!r}, second_name={self.second_name!r}, phone={self.phone!r}, addresses={self.addresses!r})"

class Phone(Base):
    __tablename__ = "phone"
    phone_id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(30))
    customers_id: Mapped[int] = mapped_column(ForeignKey("customers.customers_id")) 
    def __repr__(self) -> str:
        return f"Phone(phone_id={self.phone_id!r}, phone={self.name!r})"

class Post(Base):
    __tablename__ = "post"
    post_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    pay: Mapped[int] = mapped_column()
    def __repr__(self) -> str:
        return f"Post(post_id={self.post_id!r}, name={self.name!r}, pay={self.pay!r})"

class Product(Base):
    __tablename__ = "product"
    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    pay: Mapped[int] = mapped_column()





from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/gg", echo=True)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)