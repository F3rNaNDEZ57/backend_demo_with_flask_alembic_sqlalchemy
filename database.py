from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine("sqlite:///database.db")
# create session
Session = sessionmaker(bind=engine)