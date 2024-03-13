from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, DATE, ForeignKey
from models import Base, Motorista, Veiculo

class CtVinculo(Base):
    _tablename_= "CTVINCULO"
    id:               Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True,autoincrement=True)
    dtVinculo:        Mapped[DATE]= mapped_column(DATE,    nullable=False)
    dtDesvinculo:     Mapped[DATE]= mapped_column(DATE,    nullable=True)
    motoristaIdMotora:Mapped[int] = mapped_column(Integer, ForeignKey(Motorista.idMotora))
    veiculoIdVeic:    Mapped[int] = mapped_column(Integer, ForeignKey(Veiculo.idVeic))
