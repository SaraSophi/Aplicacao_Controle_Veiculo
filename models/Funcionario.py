from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, DATE, ForeignKey
from models import Base, Pessoa

class Funcionario(Base):
    _tablename_ = "FUNCIONARIO"
    nrMatricula:   Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True, primary_key=True)
    nmfuncionario: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    dsFuncao:      Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    dtAdmissao:    Mapped[DATE]= mapped_column(DATE, nullable=False)
    pessoaIdPessoa:Mapped[int] = mapped_column(Integer, ForeignKey(Pessoa.idPessoa))