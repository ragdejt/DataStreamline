from dataclasses import dataclass
from functions.ctk import *
from classes.Appointment import Appointment
@dataclass
class Menu:
    def main_menu():
        def appointment_menu():
            app = ctk_app("DataStreamline - AGENDAMENTOS", "300x200")
            app.grid_columnconfigure(0, weight=1)
            app.grid_rowconfigure(0, weight=1)
            # Frame esquerda.
            frame0 = ctk_frame(app, 0, 0, "nsew")
            frame0.grid_columnconfigure(0, weight=3)
            ctk_button(frame0, "Adicionar", 0, 0, "nsew", lambda: Appointment.add())
            app.mainloop()
        
        app = ctk_app("DataStreamline - MENU PRINCIPAL", "1000x1000")
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=4)
        app.grid_rowconfigure(0, weight=1)

        # Frame esquerda.
        frame0 = ctk_frame(app, 0, 0, "nsew")
        frame0.grid_columnconfigure(0, weight=1)

        ctk_button(frame0, "Agendamento", 0, None, "nsew", lambda: appointment_menu())
        ctk_button(frame0, "Fornecedor", 0, None, "nsew", None)
        ctk_button(frame0, "Funcionario", 0, None, "nsew", None)
        ctk_button(frame0, "Usuario", 0, None, "nsew", None)
        ctk_button(frame0, "Recebimento", 0, None, "nsew", None)
        ctk_button(frame0, "Carregamento", 0, None, "nsew", None)

        # Frame direita.
        frame1 = ctk_frame(app, 1, 0, "nsew")
        frame1.grid_columnconfigure(1, weight=1)

        app.mainloop()
