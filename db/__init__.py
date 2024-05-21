from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(bind=engine)
LocalSession = scoped_session(Session)

from .models import Base, Quote

