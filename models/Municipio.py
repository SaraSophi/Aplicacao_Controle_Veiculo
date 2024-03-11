from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, ForeignKey
from models import Base, Uf

class Municipio(Base):
    _tablename_ = "Municipio"
    cdMunicipio: Mapped[int] = mapped_column(Integer,      nullable=False, autoincrement=True, primary_key=True)
    nmMunicipio: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    ufCdUF:      Mapped[int] = mapped_column(Integer, ForeignKey(Uf.idUf))