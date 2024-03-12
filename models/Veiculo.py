from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR, SMALLINT, DATE
from models import Base

class Veiculo(Base):
    _tablename_ = "VEICULO"
    idVeic:        Mapped[int] = mapped_column(Integer,     nullable=False, autoincrement=True, primary_key=True)
    nrPlaca:       Mapped[str] = mapped_column(CHAR(7),     nullable=False, unique=True)
    tpCombustivel: Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    anoVeic:       Mapped[int] = mapped_column(SMALLINT,    nullable=False)
    nrRenavam:     Mapped[int] = mapped_column(Integer(11), nullable=False, unique=True)
    nrChassi:      Mapped[str] = mapped_column(VARCHAR(17), nullable=False, unique=True)
    dsModelo:      Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    dsMarca:       Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    dtAquisicao:   Mapped[DATE]= mapped_column(DATE,        nullable=False)
    dsCor:         Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    tpTracao:      Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    qtEixo:        Mapped[int] = mapped_column(SMALLINT,    nullable=False)
    nrFrota:       Mapped[int] = mapped_column(Integer(5),  nullable=False)
    nrConjunto:    Mapped[int] = mapped_column(Integer(5),  nullable=False)
