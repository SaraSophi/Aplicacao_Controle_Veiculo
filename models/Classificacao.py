from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR
from models import Base

class Classificacao(Base):
    _tablename_ = "Classificacao"
    idClassificacao:  Mapped[int] = mapped_column(Integer,     nullable=False, autoincrement=True, primary_key=True)
    dsClassificacao:  Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
  
