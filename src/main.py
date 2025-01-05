from classes.User import User
from constants.constant import *
from log.log import log_geral
from classes.Employee import Employee
from classes.Supplier import Supplier


ADMIN = User(
    ID=1,
    NOME="ADMIN",
    SENHA="ADMIN"
)

def main():
    SCRIPT_FOLDER.mkdir(exist_ok=True)
    DB_FOLDER.mkdir(exist_ok=True)
    EMPLOYEE_FOLDER.mkdir(exist_ok=True)
    SUPPLIER_FOLDER.mkdir(exist_ok=True)
    LOG_FOLDER.mkdir(exist_ok=True)

    LOGGER = log_geral()
    LOGGER.debug("DataStreamline - ")
    LOGGER.debug("DataStreamline - Verificando arquivos necessarios!.")

    User.create_db()

    User.add_info_User(ADMIN)
    
    Supplier.create_db()
    
    Employee.create_db()

    Supplier.add()
if __name__ == "__main__":
    main()