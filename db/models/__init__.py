from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


from .quotes import Quote