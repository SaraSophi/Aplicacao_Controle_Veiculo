from urllib.parse import quote
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import scoped_session, sessionmaker
import cx_Oracle
# conn = cx_Oracle.connect('system/ksl1708@localhost')

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

db_session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

# Definir a consulta SQL
sql = "SELECT * FROM uf"

# Executar a consulta
# cursor = conn.cursor()
# cursor.execute(sql)

# Iterar sobre os resultados e imprimir no console
''' for row in cursor:
    print(row) '''

# Fechar o cursor e a conexão
# cursor.close()
# conn.close()

response = db_session.execute(text('SELECT * FROM teste'))
for row in response:
   print(row)





# As seguintes linhas não são usadas no código e estão comentadas
# from sqlalchemy.orm import DeclarativeMeta, Mapped
# from sqlalchemy import Integer, VARCHAR, DATE, NUMERIC, ForeignKey
# import datetime
# from sqlalchemy.schema import Sequence
