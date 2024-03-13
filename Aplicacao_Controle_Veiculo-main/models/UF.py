from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR
from models import Base


class Uf(Base):
    _tablename_ = "UF"
    #id ou codigo? - > ajustar na tabela municipio
    cdUf:    Mapped[int] = mapped_column(Integer,      nullable=False, autoincrement=True, primary_key=True)
    nmUf:    Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    dsSigla: Mapped[str] = mapped_column(CHAR(2),      nullable=False)