from pathlib import Path

SCRIPT_FOLDER = Path.home() / ("DataStreamline")



DB_FOLDER = SCRIPT_FOLDER / ("BANCO DE DADOS")

LOG_FOLDER = SCRIPT_FOLDER / ("REGISTROS")

# Users.
DB_TABLE_USER = "USUARIOS"
DB_USER = DB_FOLDER / ("USUARIOS.db")

# Costumers.
DB_TABLE_COSTUMER = "CLIENTES"
DB_COSTUMER = DB_FOLDER / ("CLIENTES.db")

# Suppliers.
SUPPLIER_FOLDER = SCRIPT_FOLDER / ("FORNECEDORES")
DB_SUPPLIER = DB_FOLDER / ("FORNECEDORES.db")
DB_TABLE_SUPPLIER = "FORNECEDORES"
SUPPLIER_COLUMNS = [
    "RAZAO_SOCIAL",
    "NOME_FANTASIA",
    "CNPJ",
    "INSCRICAO_ESTADUAL",
    "INSCRICAO_MUNICIPAL",
    "CONTRATO",
    "ENDERECO",
    "ESTADO",
    "CIDADE",
    "TELEFONE",
    "EMAIL",
    "TITULAR_CONTA",
    "BANCO",
    "AGENCIA",
    "CONTA",
    "REPRESENTANTE_LEGAL",
    "CARGO",
    "DOC_IDENTIDADE",
]

# Employee.
EMPLOYEE_FOLDER = SCRIPT_FOLDER / ("FUNCIONARIOS")
DB_EMPLOYEE = DB_FOLDER / ("FUNCIONARIOS.db")
DB_TABLE_EMPLOYEE = "FUNCIONARIOS"
EMPLOYEE_COLUMNS = [
    "NOME",
    "NASCIMENTO",
    "SEXO",
    "CARGO",
    "ADMISSAO",
    "SALARIO",
    "CTPS",
    "RG",
    "CPF",
    "ESTADO_CIVIL",
    "CONTRATO",
    "ESCOLARIDADE",
    "ENDERECO",
    "CIDADE",
    "ESTADO",
    "TELEFONE",
    "EMAIL"
]

# Appointment.
APPOINTMENT_FOLDER = SCRIPT_FOLDER / ("AGENDAMENTOS")
DB_APPOINTMENT = DB_FOLDER / ("AGENDAMENTOS.db")
DB_TABLE_APPOINTMENT = "AGENDAMENTOS"
APPOINTMENT_COLUMNS = [
    "NOME_FANTASIA",
    "DATA_AGENDAMENTO",
    "HORARIO_AGENDAMENTO"
]

MASC_FEM = ["Masculino", "Feminino"]
#
POSITION = [
    "Auxiliar Administrativo",
    "Gerente Administrativo",
    "Vendedor Jr",
    "Vendedor Senior",
    "Vendedor Pleno",
    "Gerente Comercial",
    "Auxiliar logistico",
    "Conferente",
    "Gerente Logistico"
]
STATUS = ["Solteiro", "Casado"]

CONTRACT = ["CLT", "PJ"]

EDUCATION = [
    "Ensino Fundamental Completo",
    "Ensino Fundamental Incompleto",
    "Ensino Médio Completo",
    "Ensino Médio Incompleto",
    "Ensino Superior Completo",
    "Ensino Superior Incompleto"
]

STATE = [
    "Acre (AC)",
    "Alagoas (AL)",
    "Amapá (AP)",
    "Amazonas (AM)",
    "Bahia (BA)",
    "Ceará (CE)",
    "Distrito Federal (DF)",
    "Espírito Santo (ES)",
    "Goiás (GO)",
    "Maranhão (MA)",
    "Mato Grosso (MT)",
    "Mato Grosso do Sul (MS)",
    "Minas Gerais (MG)",
    "Pará (PA)",
    "Paraíba (PB)",
    "Paraná (PR)",
    "Pernambuco (PE)",
    "Piauí (PI)",
    "Rio de Janeiro (RJ)",
    "Rio Grande do Norte (RN)",
    "Rio Grande do Sul (RS)",
    "Rondônia (RO)",
    "Roraima (RR)",
    "Santa Catarina (SC)",
    "São Paulo (SP)",
    "Sergipe (SE)",
    "Tocantins (TO)"
]

BANK = [
    "Banco do Brasil (BB) - 001",
    "Caixa Econômica Federal (Caixa) - 104",
    "Itaú Unibanco - 341",
    "Bradesco - 237",
    "Santander Brasil - 033",
    "Nubank - 260",
    "Banco Inter - 077",
    "BTG Pactual - 208",
    "C6 Bank - 336",
    "Banco Safra - 422"
]
