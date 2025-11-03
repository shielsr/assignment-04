from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()



class Customer(db.Model):
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[int] = mapped_column(nullable=False)
 
    orders = db.relationship('Order', back_populates='customer')
    pumpkin = db.relationship('PumpkinDesign', back_populates='designer')

    def __repr__(self):
        return f"User(name='{self.name}')"


 class Order(db.Model):
    order_id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False,  default=lambda: datetime.now(timezone.utc))
    customer: Mapped[int] = mapped_column(nullable=False) 
    pumpkin_id: mapped_column(db.ForeignKey('pumpkin_design.customer_id'), nullable=False) 
    fulfilment: Mapped[str] = mapped_column(nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customer.customer_id'), nullable=False)
     
    customer = db.relationship('Customer', back_populates='orders') 
    pumpkin = db.relationship('PumpkinDesign', back_populates='order')
    def __repr__(self):
        return f"Order (orderId='{self.order_id}', customerId='{self.customer_id}', pumpkinId='{self.pumpkin_id}', fulfilment='{self.fulfilment}')"
    

class PumpkinDesign(db.Model):
    design_id: Mapped[int] = mapped_column(primary_key=True)
    size: Mapped[str] = mapped_column(nullable=False) 
    eyes: Mapped[str] = mapped_column(nullable=False)
    mouth: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False,  default=lambda: datetime.now(timezone.utc))
    order_id: Mapped[int] = mapped_column(db.ForeignKey('order.order_id'), nullable=False)

    designer = db.relationship('Customer', back_populates='pumpkin')
    order = db.relationship('Order', back_populates='pumpkin')



    def __repr__(self):
        return f"Pumpkin Design (id='{self.design_id}', size='{self.size}', eyes='{self.eyes}', mouth='{self.mouth}')"
    
 