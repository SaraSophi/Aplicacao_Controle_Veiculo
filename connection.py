''' from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, session
import cx_Oracle

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(url = instance, echo=True, max_identifier_length=30)

session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

# Executar a consulta
response = session.execute(text('SELECT * FROM uf'))

#response = session.add("CDUF= 11, NMUF = 'RAMOS', DSSIGLA = 'BR'")

response = session.execute(text("insert into uf (CDUF, NMUF, DSSIGLA) values (5,'testes','TE')"))

session.commit()
for row in response:
 print(row)



# As seguintes linhas não são usadas no código e estão comentadas
# from sqlalchemy.orm import DeclarativeMeta, Mapped
# from sqlalchemy import Integer, VARCHAR, DATE, NUMERIC, ForeignKey
# import datetime
# from sqlalchemy.schema import Sequence
'''

from urllib.parse import quote
from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import scoped_session, sessionmaker
import cx_Oracle

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(url=instance, echo=True, max_identifier_length=30)

db_session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

# Realize a atualização no banco de dados
try:
    # Inicie uma transação
    with db_session.begin():
        # Execute a atualização
        stmt = text("UPDATE uf SET NMUF = 'testes' WHERE CDUF = 5")
        db_session.execute(stmt)
    # Commit da transação
    db_session.commit()
    print("Atualização bem-sucedida.")
except Exception as e:
    # Em caso de erro, faça o rollback da transação
    db_session.rollback()
    print("Erro durante a atualização:", e)
finally:
    # Feche a sessão
    db_session.close()
