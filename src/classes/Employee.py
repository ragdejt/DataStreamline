import sqlite3
import shutil
import pandas
from functions.ctk import *
from tkinter import messagebox
from constants.constant import *
from dataclasses import dataclass
from log.log import log_geral


@dataclass
class Employee:
    NOME:str
    NASCIMENTO:str
    SEXO:str
    CARGO:str
    ADMISSAO:str
    SALARIO:float
    CTPS:int
    RG:int
    CPF:int
    ESTADO_CIVIL:str
    CONTRATO:int
    ESCOLARIDADE:str
    ENDERECO:str
    CIDADE:str
    ESTADO:str
    TELEFONE:str
    EMAIL:str
    
    def create_db():
        LOGGER = log_geral()

        LOGGER.debug(f"DataStreamline - Conectando ao banco de dados: {DB_EMPLOYEE}")
        LOGGER.debug(f"DataStreamline - Verificando se existe a tabela: {DB_TABLE_EMPLOYEE}")
        with sqlite3.connect(DB_EMPLOYEE) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_EMPLOYEE} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            NASCIMENTO TEXT NOT NULL,
            SEXO TEXT NOT NULL,
            CARGO TEXT NOT NULL,
            ADMISSAO TEXT NOT NULL,
            SALARIO TEXT NOT NULL,
            CTPS TEXT NOT NULL,
            RG TEXT NOT NULL,
            CPF TEXT NOT NULL,
            ESTADO_CIVIL TEXT NOT NULL,
            CONTRATO TEXT NOT NULL,
            ESCOLARIDADE TEXT NOT NULL,
            ENDERECO TEXT NOT NULL,
            CIDADE TEXT NOT NULL,
            ESTADO TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            EMAIL TEXT NOT NULL            
            )
            """)
        connect.commit()

    def add():
        def button():
            new_data = {
                "NOME":[NOME.get()],
                "NASCIMENTO":[NASCIMENTO.get()],
                "SEXO":[SEXO.get()],
                "CARGO":[CARGO.get()],
                "ADMISSAO":[ADMISSAO.get()],
                "SALARIO":[SALARIO.get()],
                "CTPS":[CTPS.get()],
                "RG":[RG.get()],
                "CPF":[CPF.get()],
                "ESTADO_CIVIL":[ESTADO_CIVIL.get()],
                "CONTRATO":[CONTRATO.get()],
                "ESCOLARIDADE":[ESCOLARIDADE.get()],
                "ENDERECO":[ENDERECO.get()],
                "CIDADE":[CIDADE.get()],
                "ESTADO":[ESTADO.get()],
                "TELEFONE":[TELEFONE.get()],
                "EMAIL":[EMAIL.get()]
            }
            path_file = EMPLOYEE_FOLDER / (new_data["NOME"][0])
            path_file.mkdir(exist_ok=True)
            with pandas.ExcelWriter(path=path_file / f"{new_data["NOME"][0]}.xlsx", engine="xlsxwriter") as writer:
                pandas.DataFrame(columns=EMPLOYEE_COLUMNS, data=new_data).to_excel(writer, sheet_name=new_data["NOME"][0], index=False)

            shutil.copy(admission_path.get(), path_file / ("Exame admissional.pdf"))
            shutil.copy(ctps_path.get(), path_file / ("Carteira de trabalho profissional.pdf"))
            shutil.copy(rg_path.get(), path_file / ("Registro Geral.pdf"))
            shutil.copy(cpf_path.get(), path_file / ("Cadastro de pessoa fisica.pdf"))
            shutil.copy(contract_path.get(), path_file / ("Contrato.pdf"))
            shutil.copy(education_path.get(), path_file / ("Comprovante de escolaridade.pdf"))
            shutil.copy(address_path.get(), path_file / ("Comprovante de endereço.pdf"))

            messagebox.showinfo("DataStreamline", "Informação Cadastrada!")

            app.destroy()

        # Frame App.
        app = ctk_app("DataStreamline - ADICIONAR FUNCIONARIO", "1000x1000")
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=3)
        app.grid_rowconfigure(0, weight=1)

        # Frame esquerda.
        frame0 = ctk_frame(app, 0, 0, "nsew")
        frame0.grid_columnconfigure(0, weight=1)

        NOME = ctk_entry(frame0, "Nome completo", 0, None, "nsew")
        NASCIMENTO = ctk_entry(frame0, "Data de Nascimento", 0 , None, "nsew")
        SEXO = ctk_menu_opt(frame0, MASC_FEM, 0, None, "nsew")
        CARGO = ctk_menu_opt(frame0, POSITION, 0, None, "nsew")
        ADMISSAO = ctk_entry(frame0, "Data de Admissão", 0 , None, "nsew")
        SALARIO = ctk_entry(frame0, "Salario", 0 , None, "nsew")
        CTPS = ctk_entry(frame0, "Carteira de Trabalho Profissional. (CTPS)", 0 , None, "nsew")
        RG = ctk_entry(frame0, "Registro Geral. (RG)", 0 , None, "nsew")
        CPF = ctk_entry(frame0, "Cadastro de Pessoa Fisica. (CPF)", 0 , None, "nsew")
        ESTADO_CIVIL = ctk_menu_opt(frame0, STATUS, 0, None, "nsew")
        CONTRATO = ctk_menu_opt(frame0, CONTRACT, 0, None, "nsew")
        ESCOLARIDADE = ctk_menu_opt(frame0, EDUCATION, 0, None, "nsew")
        ENDERECO = ctk_entry(frame0, "Endereço", 0 , None, "nsew")
        CIDADE = ctk_entry(frame0, "Cidade", 0, None, "nsew")
        ESTADO = ctk_menu_opt(frame0, None, 0, None, "nsew")
        TELEFONE = ctk_entry(frame0, "Telefone", 0 , None, "nsew")
        EMAIL = ctk_entry(frame0, "Email", 0 , None, "nsew")

        # Frame direita.
        frame1 = ctk_frame(app, 1, 0, "nsew")
        frame1.grid_columnconfigure(0, weight=1)
        
        admission_path = ctk_entry(frame1, "Arquivo: Exame admissional", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(admission_path))

        ctps_path = ctk_entry(frame1, "Arquivo: Carteira de trabalho(CTPS)", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(ctps_path))

        rg_path = ctk_entry(frame1, "Arquivo: Registro Geral(RG)", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(rg_path))

        cpf_path = ctk_entry(frame1, "Arquivo: Cadastro de pessoa fisica(CPF)", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(cpf_path))

        contract_path = ctk_entry(frame1, "Arquivo: Contrato de trabalho", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(contract_path))

        education_path = ctk_entry(frame1, "Arquivo: Comprovante de escolaridade", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(education_path))

        address_path = ctk_entry(frame1, "Arquivo: Comprovante de endereço", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(address_path))

        ctk_button(frame0, "Cadastrar", 0, None, "nsew", lambda: button())

        app.mainloop()

        

    def remove(self):
        # Abrir o app, com a tela pedindo id para remover. Abrir uma tela pedindo confirmaçao se esse sao os dados que deseja remover do banco de dados.
        pass