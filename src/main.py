from log.log import log_geral
from classes.Menu import Menu
from classes.User import User
from classes.User import ADMIN
from classes.Login import Login
from constants.constant import *
from classes.Employee import Employee
from classes.Supplier import Supplier
from classes.Appointment import Appointment
        
def main():
    SCRIPT_FOLDER.mkdir(exist_ok=True)
    LOG_FOLDER.mkdir(exist_ok=True)
    DB_FOLDER.mkdir(exist_ok=True)

    LOGGER = log_geral()
    LOGGER.debug("DataStreamline - Verificando arquivos [...]")

    Employee.create_db()
    EMPLOYEE_FOLDER.mkdir(exist_ok=True)

    Supplier.create_db()
    SUPPLIER_FOLDER.mkdir(exist_ok=True)

    Appointment.create_db()
    APPOINTMENT_FOLDER.mkdir(exist_ok=True)

    User.create_db()
    User.add_info_User(ADMIN)

    LOGGER.debug("DataStreamline - Iniciando Aplicação!")
    Login.login()



if __name__ == "__main__":
    main()

