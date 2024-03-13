from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, ForeignKey
from models import Base, Funcionario

class Motorista(Base):
    _tablename_ = "MOTORISTA"
    idMotora:              Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True, primary_key=True)
    nmMotora:              Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    funcionarioNrMatricula:Mapped[int] = mapped_column(Integer, ForeignKey(Funcionario.nrMatricula))