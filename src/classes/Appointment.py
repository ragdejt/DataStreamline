import time
import pandas
import sqlite3
from tkinter import messagebox
from functions.ctk import *
from dataclasses import dataclass
from classes.Supplier import Supplier
from log.log import log_geral
from constants.constant import *

@dataclass
class Appointment(Supplier):
    APPOINTMENT:str
    
    def create_db():
        LOGGER = log_geral()

        LOGGER.debug(f"DataStreamline - Conectando ao banco de dados: {DB_APPOINTMENT}")
        LOGGER.debug(f"DataStreamline - Verificando se existe a tabela: {DB_TABLE_APPOINTMENT}")
        with sqlite3.connect(DB_APPOINTMENT) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_APPOINTMENT}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME_FANTASIA TEXT NOT NULL,
            DATA_AGENDAMENTO TEXT NOT NULL,
            HORARIO_AGENDAMENTO TEXT NOT NULL           
            )
            """)
        connect.commit()



    def add():
        def button():
            LOGGER = log_geral()
            LOGGER.debug("DataStreamline - Adicionar novo agendamento.")
            new_data = {
                "NOME_FANTASIA":[nome_fantasia.get()],
                "DATA_AGENDAMENTO":[data_agendamento.get()],
                "HORARIO_AGENDAMENTO":[horario_agendamento.get()]
            }
            date = time.strftime("%Y%m%d%H%M%S")
            with pandas.ExcelWriter(path=APPOINTMENT_FOLDER / (f"Appointment{date}.xlsx"), engine="xlsxwriter") as writer:
                pandas.DataFrame(data=new_data, columns=APPOINTMENT_COLUMNS).to_excel(writer, sheet_name=f"{date}", index=False)

            LOGGER.debug(f"DataStreamline - Agendamento: {date}, Salvo!")
            
            messagebox.showinfo("DataStreamline", "Informação Cadastrada!")

            app.destroy()

        DADOS = []
        with sqlite3.connect(DB_SUPPLIER) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""SELECT NOME_FANTASIA FROM FORNECEDORES""")
            result = cursor.fetchall()
            for row in result:
                DADOS.append(row[0])

            


        # Frame App.
        app = ctk_app("DataStreamline - ADICIONAR AGENDAMENTO", "500x200")
        app.grid_columnconfigure(0, weight=1)
        app.grid_rowconfigure(0, weight=1)
        # Frame esquerda.
        frame0 = ctk_frame(app, 0, 0, "nsew")
        frame0.grid_columnconfigure(0, weight=1)

        nome_fantasia = ctk_menu_opt(frame0, DADOS, 0, None, "nsew")
        data_agendamento = ctk_entry(frame0, "Data do Agendamento", 0, None, "nsew")
        horario_agendamento = ctk_entry(frame0, "Horario do Agendamento", 0 , None, "nsew")

        ctk_button(frame0, "Cadastrar", 0, None, "s", lambda: button())


            
        app.mainloop()
