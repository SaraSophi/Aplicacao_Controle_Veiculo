from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import cx_Oracle

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedns(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(instance, echo=True, max_identifier_length=30)

bd_session = scoped_session(sessionmaker(autocommit=False, autoFlush=False, bind=engine))

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Interger, VARCHAR, DATE, NUMERIC ForeignKey
import datetime
