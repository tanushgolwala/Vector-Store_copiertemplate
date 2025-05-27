from sqlalchemy import Column, String, LargeBinary
from app.db import Base

class VectorEntry(Base):
    __tablename__ = "vectors"
    id = Column(String, primary_key=True)
    text = Column(String, nullable=False)
    embedding = Column(LargeBinary, nullable=False)
