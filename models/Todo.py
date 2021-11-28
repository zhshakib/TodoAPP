from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite Database
engine = create_engine("sqlite:///todo.db")

# Create a DeclaraiveMeta Instances
Base = declarative_base()


# TODO Tables!
class TODO(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))


# Create The Database!
Base.metadata.create_all(engine)
