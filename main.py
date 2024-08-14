import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyautogui
import os
import webbrowser
from time import sleep


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # Variaveis do formulário
        self.name = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")

        # cabeçalho do formulário
        hdr_txt = "Entre com seu usuário e senha para inicializar o sistema"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # Entradas do formulário
        self.create_form_entry("Usuário", self.name)
        self.create_form_entry("Senha", self.password, show="*")
        self.create_buttonbox()

    def create_form_entry(self, label, variable, show=None):
        """Cria o formulário de entrada"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable, show=show)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Cria os botões de submissão e cancelamento."""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Login",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancelar",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        begin(self.name.get(), self.password.get())
        self.quit()

    def on_cancel(self):
        """Fecha a aplicação."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("Nossa Hepta", "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()
