from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR
from models import Base

class TpVeiculo(Base):
    _tablename_ = "TipoVeiculo"
    idTpVeiculo:   Mapped[int] = mapped_column(Integer,     nullable=False, autoincrement=True, primary_key=True)
    dsModelo:      Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
   
