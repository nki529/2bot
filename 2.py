from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class TBaseControler:
    def __init__(self, URL) -> None:
        engine=self.engine = create_engine("sqlite://", echo=True)



