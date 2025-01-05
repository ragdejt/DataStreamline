import shutil
import pandas
import sqlite3
from tkinter import messagebox
from dataclasses import dataclass
from functions.ctk import *
from constants.constant import *
from log.log import log_geral

@dataclass
class Supplier:
    ID:int
    NOME:str
    CNPJ:str
    EMAIL:str
    TELEFONE:str
    ENDERECO:str
    ESTADO:str
    CIDADE:str
    BANCO:int
    AGENCIA:int
    CONTA:int

    def create_db():
        LOGGER = log_geral()

        LOGGER.debug(f"DataStreamline - Conectando ao banco de dados: {DB_SUPPLIER}")
        LOGGER.debug(f"DataStreamline - Verificando se existe a tabela: {DB_TABLE_SUPPLIER}")
        with sqlite3.connect(DB_SUPPLIER) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_SUPPLIER}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            RAZAO_SOCIAL TEXT NOT NULL,
            NOME_FANTASIA TEXT NOT NULL,
            CNPJ TEXT NOT NULL,
            INSCRICAO_ESTADUAL TEXT NOT NULL,
            INSCRICAO_MUNICIPAL TEXT NOT NULL,
            CONTRATO TEXT NOT NULL,
            ENDERECO TEXT NOT NULL,
            ESTADO TEXT NOT NULL,
            CIDADE TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            TITULAR_CONTA TEXT NOT NULL,
            BANCO TEXT NOT NULL,
            AGENCIA TEXT NOT NULL,
            CONTA TEXT NOT NULL,
            REPRESENTANTE_LEGAL TEXT NOT NULL,
            CARGO TEXT NOT NULL,
            DOC_IDENTIDADE TEXT NOT NULL              
            )
            """)
        connect.commit()
    def add():
        def button():
            LOGGER = log_geral()

            LOGGER.debug("DataStreamline - Adicionar Novo Fornecedor")
            new_data = {
                "RAZAO_SOCIAL":[RAZAO_SOCIAL.get()],
                "NOME_FANTASIA":[NOME_FANTASIA.get()],
                "CNPJ":[CNPJ.get()],
                "INSCRICAO_ESTADUAL":[INSCRICAO_ESTADUAL.get()],
                "INSCRICAO_MUNICIPAL":[INSCRICAO_MUNICIPAL.get()],
                "CONTRATO":[CONTRATO.get()],
                "ENDERECO":[ENDERECO.get()],
                "ESTADO":[ESTADO.get()],
                "CIDADE":[CIDADE.get()],
                "TELEFONE":[TELEFONE.get()],
                "EMAIL":[EMAIL.get()],
                "TITULAR_CONTA":[TITULAR_CONTA.get()],
                "BANCO":[BANCO.get()],
                "AGENCIA":[AGENCIA.get()],
                "CONTA":[CONTA.get()],
                "REPRESENTANTE_LEGAL":[REPRESENTANTE_LEGAL.get()],
                "CARGO":[CARGO.get()],
                "DOC_IDENTIDADE":[IDENTIDADE.get()]
            }
            
            path_file = SUPPLIER_FOLDER / (new_data["NOME_FANTASIA"][0])

            LOGGER.debug(f"DataStreamline - Criando pasta: {path_file}")
            path_file.mkdir(exist_ok=True)

            LOGGER.debug(f"DataStreamline - Criando planilha: {new_data["NOME_FANTASIA"][0]}")
            with pandas.ExcelWriter(path_file / (f"{new_data["NOME_FANTASIA"][0]}.xlsx"), engine="xlsxwriter") as writer:
                pandas.DataFrame(columns=SUPPLIER_COLUMNS, data=new_data).to_excel(writer, sheet_name=new_data["NOME_FANTASIA"][0], index=False)
            
            LOGGER.debug(f"DataStreamline - Conectando ao banco de dados: {DB_SUPPLIER}")
            LOGGER.debug(f"DataStreamline - Inserindo dados!")
            with sqlite3.connect(DB_SUPPLIER) as connect:
                cursor = connect.cursor()
                cursor.execute(f"""
                INSERT OR IGNORE INTO {DB_TABLE_SUPPLIER}(
                RAZAO_SOCIAL,
                NOME_FANTASIA,
                CNPJ,
                INSCRICAO_ESTADUAL,
                INSCRICAO_MUNICIPAL,
                CONTRATO,
                ENDERECO,
                ESTADO,
                CIDADE,
                TELEFONE,
                EMAIL,
                TITULAR_CONTA,
                BANCO,
                AGENCIA,
                CONTA,
                REPRESENTANTE_LEGAL,
                CARGO,
                DOC_IDENTIDADE
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(
                new_data["RAZAO_SOCIAL"][0],
                new_data["NOME_FANTASIA"][0],
                new_data["CNPJ"][0],
                new_data["INSCRICAO_ESTADUAL"][0],
                new_data["INSCRICAO_MUNICIPAL"][0],
                new_data["CONTRATO"][0],
                new_data["ENDERECO"][0],
                new_data["ESTADO"][0],
                new_data["CIDADE"][0],
                new_data["TELEFONE"][0],
                new_data["EMAIL"][0],
                new_data["TITULAR_CONTA"][0],
                new_data["BANCO"][0],
                new_data["AGENCIA"][0],
                new_data["CONTA"][0],
                new_data["REPRESENTANTE_LEGAL"][0],
                new_data["CARGO"][0],
                new_data["DOC_IDENTIDADE"][0]
                ))
            connect.commit()

            shutil.copy(File1.get(), path_file / ("Comprovante_de_Inscricao_e_de_Situacao_Cadastral.pdf"))
            LOGGER.debug(f"DataStreamline - Arquivo: Comprovante de Inscrição e de Situação Cadastral no CNPJ - COPIADO")

            shutil.copy(File2.get(), path_file / ("Certidao_Negativa_de_Debitos.pdf"))
            LOGGER.debug(f"DataStreamline - Arquivo: Certidão Negativa de Débitos (CND) - COPIADO")

            shutil.copy(File3.get(), path_file / ("Certidao_Negativa_de_Debitos_Trabalhistas.pdf"))
            LOGGER.debug(f"DataStreamline - Arquivo: Certidão Negativa de Débitos Trabalhistas (CNDT) - COPIADO")

            shutil.copy(File4.get(), path_file / ("Comprovante_de_Endereco_Comercial.pdf"))
            LOGGER.debug(f"DataStreamline - Arquivo: Comprovante de Endereço Comercial - COPIADO")

            shutil.copy(File5.get(), path_file / ("Alvara_de_Funcionamento.pdf"))
            LOGGER.debug(f"DataStreamline - Arquivo: Alvará de Funcionamento - COPIADO")

            messagebox.showinfo("DataStreamline - ADICIONAR FORNECEDOR", "Informação Cadastrada.")
            LOGGER.debug(f"DataStreamline - Fornecedor: {new_data["NOME_FANTASIA"][0]} - Cadastrado!")

            app.destroy()
        
        # Frame App.
        app = ctk_app("DataStreamline - ADICIONAR FORNECEDOR", "1000x1000")
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=3)
        app.grid_rowconfigure(0, weight=1)
        # Frame esquerda.
        frame0 = ctk_frame(app, 0, 0, "nsew")
        frame0.grid_columnconfigure(0, weight=1)
        RAZAO_SOCIAL = ctk_entry(frame0, "Razão Social.", 0, None, "nsew")
        NOME_FANTASIA = ctk_entry(frame0, "Nome Fantasia.", 0 , None, "nsew")
        CNPJ = ctk_entry(frame0, "Cadastro Nacional de Pessoa Juridica. (CNPJ)", 0 , None, "nsew")
        INSCRICAO_ESTADUAL = ctk_entry(frame0, "Inscrição Estadual.", 0 , None, "nsew")
        INSCRICAO_MUNICIPAL = ctk_entry(frame0, "Inscrição Municipal.", 0 , None, "nsew")
        CONTRATO = ctk_menu_opt(frame0, CONTRACT, 0, None, "nsew")
        ENDERECO = ctk_entry(frame0, "Endereço.", 0 , None, "nsew")
        ESTADO = ctk_menu_opt(frame0, None, 0, None, "nsew")
        CIDADE = ctk_entry(frame0, "Cidade.", 0, None, "nsew")
        TELEFONE = ctk_entry(frame0, "Telefone/Contato.", 0 , None, "nsew")
        EMAIL = ctk_entry(frame0, "Email.", 0 , None, "nsew")
        TITULAR_CONTA = ctk_entry(frame0, "Titular da conta.", 0, None, "nsew")
        BANCO = ctk_menu_opt(frame0, BANK, 0, None, "nsew")
        AGENCIA = ctk_entry(frame0, "Agência", 0, None, "nsew")
        CONTA = ctk_entry(frame0, "Conta", 0, None, "nsew")
        REPRESENTANTE_LEGAL = ctk_entry(frame0, "Representante Legal", 0, None, "nsew")
        CARGO = ctk_menu_opt(frame0, POSITION, 0, None, "nsew")
        IDENTIDADE = ctk_entry(frame0, "Documento de Identidade", 0, None, "nsew")
        # Frame direita.
        frame1 = ctk_frame(app, 1, 0, "nsew")
        frame1.grid_columnconfigure(0, weight=1)

        File1 = ctk_entry(frame1, "Arquivo: Comprovante de Inscrição e de Situação Cadastral no CNPJ", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(File1))

        File2 = ctk_entry(frame1, "Arquivo: Certidão Negativa de Débitos (CND)", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(File2))

        File3 = ctk_entry(frame1, "Arquivo: Certidão Negativa de Débitos Trabalhistas (CNDT)", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(File3))
        
        File4 = ctk_entry(frame1, "Arquivo: Comprovante de Endereço Comercial", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(File4))

        File5 = ctk_entry(frame1, "Arquivo: Alvará de Funcionamento", 0, None, "nsew")
        ctk_button(frame1, "Selecionar arquivo", 0, None, "nsew", lambda: select_file(File5))

        ctk_button(frame0, "Cadastrar", 0, None, "nsew", lambda: button())
        
        app.mainloop()
