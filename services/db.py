from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, session
import cx_Oracle

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

# Informando para o banco qual o meu usuário e senha, e o servidor em que o banco está
USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(url = instance, echo=True, max_identifier_length=30)




from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, DATE, ForeignKey
from models import Base, Pessoa



class Endereco(Base):
    _tablename_= "Endereco"
    idEndereco:          Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
    dsLogradouro:        Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nrCasa:              Mapped[int] = mapped_column(Integer, nullable=False)
    nmBairro:            Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nrCep:               Mapped[int] = mapped_column(Integer(8), nullable=False)
    municipioCdMunicipio:Mapped[int] = mapped_column(Integer, ForeignKey(Municipio.cdMunicipio))
    pessoaIdPessoa:      Mapped[int] = mapped_column(Integer, ForeignKey(Pessoa.idPessoa))