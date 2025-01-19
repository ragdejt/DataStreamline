import sqlite3
from constants.constant import *
from classes.Menu import Menu
from dataclasses import dataclass
from functions.ctk import *
@dataclass
class Login:
    def login():
        def button():
            USERNAME = entry_user.get()
            PASSWORD = entry_pass.get()
            with sqlite3.connect(DB_USER) as connect:
                cursor = connect.cursor()
                query = "SELECT * FROM USUARIOS WHERE NOME = ? AND SENHA = ?"
                cursor.execute(query, (USERNAME, PASSWORD))
                result = cursor.fetchone()
                if result:
                    app.destroy()
                    Menu.main_menu()
                else:
                    label1.configure(text="Usuario/Senha incorretos.")


        app = ctk_app("DataStreamline - LOGIN", "500x180")
        app.grid_columnconfigure(0, weight=1)
        app.grid_rowconfigure(1, weight=1)
        label1 = ctk_label(app, "Conecte-se ao DataStreamline, e faça a diferença!", 0, None, "ew")

        frame1 = ctk_frame(app, 0, None, "nsew")
        frame1.grid_columnconfigure(0, weight=1)

        entry_user = ctk_entry(frame1, "Usuario", 0, None, "nsew")
        entry_pass = ctk_entry(frame1, "Senha", 0, None, "nsew")
        ctk_button(frame1, "Login", 0, None, "s", lambda: button())

        app.mainloop()
