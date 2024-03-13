from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, ForeignKey
from models import Base, Pessoa, Municipio

class Endereco(Base):
    _tablename_= "Endereco"
    idEndereco:          Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True,autoincrement=True)
    dsLogradouro:        Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    nrCasa:              Mapped[int] = mapped_column(Integer, nullable=False)
    nmBairro:            Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nrCep:               Mapped[int] = mapped_column(Integer(8), nullable=False)
    municipioCdMunicipio:Mapped[int] = mapped_column(Integer, ForeignKey(Municipio.cdMunicipio))
    pessoaIdPessoa:      Mapped[int] = mapped_column(Integer, ForeignKey(Pessoa.idPessoa))