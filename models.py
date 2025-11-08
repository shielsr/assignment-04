from datetime import datetime, timezone

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()



class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False, default="customer")

    orders = db.relationship('Order', back_populates='customer')

    def __repr__(self):
        return f"User(name='{self.name}', username='{self.username}', role='{self.role}')"

    def get_id(self):
        return self.user_id
    

class Order(db.Model):
    __tablename__ = 'order'
    order_id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False,  default=lambda: datetime.now(timezone.utc))
    status: Mapped[str] = mapped_column(nullable=True)

    customer_id: Mapped[int] = mapped_column(db.ForeignKey('user.user_id'), nullable=False)
    
    customer = db.relationship('User', back_populates='orders')
    pumpkins = db.relationship('PumpkinDesign', back_populates='order')  # one-to-many
     
    def __repr__(self):
        return f"Order (orderId='{self.order_id}', status='{self.status}')"


class PumpkinDesign(db.Model):
    __tablename__ = 'pumpkin_design'
    design_id: Mapped[int] = mapped_column(primary_key=True)
    size: Mapped[str] = mapped_column(nullable=False) 
    eyes: Mapped[str] = mapped_column(nullable=False)
    mouth: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False,  default=lambda: datetime.now(timezone.utc))
 
    order_id: Mapped[int] = mapped_column(db.ForeignKey('order.order_id'), nullable=True)  # can be null initially
    
    order = db.relationship('Order', back_populates='pumpkins')

    def __repr__(self):
        return f"Pumpkin Design (order_id='{self.order_id}', size='{self.size}', eyes='{self.eyes}', mouth='{self.mouth}')"
    




 