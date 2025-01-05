import sqlite3
from dataclasses import dataclass
from constants.constant import *
from log.log import log_geral
@dataclass
class User:
    ID:int
    NOME:str
    SENHA:str

    def create_db():
        LOGGER = log_geral()

        LOGGER.debug(f"DataStreamline - Conectando ao banco de dados: {DB_USER}")
        LOGGER.debug(f"DataStreamline - Verificando se existe a tabela: {DB_TABLE_USER}")
        with sqlite3.connect(DB_USER) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_USER}(
            ID INTEGER PRIMARY KEY NOT NULL,
            NOME TEXT NOT NULL,
            SENHA TEXT NOT NULL
            )
            """)
        connect.commit()
    def add_info_User(self):
        with sqlite3.connect(DB_USER) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""
            INSERT OR IGNORE INTO {DB_TABLE_USER}(ID, NOME, SENHA) VALUES (?, ?, ?)""",
            (self.ID, self.NOME, self.SENHA))