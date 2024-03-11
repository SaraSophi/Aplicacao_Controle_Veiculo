from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR, SMALLINT, DATE, NUMERIC, ForeignKey
from models import Base
from sqlalchemy.schema import Sequence

class Pessoa(Base):
    _tablename_= "PESSOA"
    idPessoa:     Mapped[int] = mapped_column(Integer, Sequence('pessoaSeq'), nullable=False, autoincrement=True, primary_key=True)
    nmPessoa:     Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nrcpf:        Mapped[str] = mapped_column(NUMERIC(11), nullable=False,unique=True)
    dtNascimento: Mapped[DATE]= mapped_column(DATE, nullable=False)