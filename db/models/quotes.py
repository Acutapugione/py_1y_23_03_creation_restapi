from . import Base
from sqlalchemy.orm import Mapped, mapped_column


class Quote(Base):
    __tablename__ = 'quotes'

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    text: Mapped[str] = mapped_column(unique=True)
