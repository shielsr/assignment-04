from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class pumpkinDesign(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    size: Mapped[str] = mapped_column(nullable=False) 
    eyes: Mapped[str] = mapped_column(nullable=False)
    mouth: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    created_at = db.mapped_column(db.DateTime, default=lambda: datetime.now(timezone.utc))    

    def __repr__(self):
        return f"Pumpkin Design (id='{self.id}', size='{self.size}', eyes='{self.eyes}', mouth='{self.mouth}')"