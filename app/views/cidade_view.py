
from app.models.cidade import Cidade

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Cidade_Terminal_View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._cidades = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de cidades")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
  

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Cidades",
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados da cidade"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_Nome = tk.Label(
            self.frm_dados,
            text = "Nome "
        )
        self.lbl_Nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_Nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_Nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_Sigla= tk.Label(
            self.frm_dados,
            text = "Sigla "
        )
        self.lbl_Sigla.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_Sigla = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_Sigla.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )        
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )        
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )   
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_fornecedores = ttk.Treeview(
            self.root,
            height = 10
        )    
        self.tbl_fornecedores.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )  


    def configurar_treeview(self):
        self.tbl_cidades["columns"] = (
            "id",
            "Nome",
            "Sigla"
        )
        self.tbl_cidades.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_cidades.column(
            "id",
            width =10
        )
        self.tbl_cidades.column(
            "nome",
            width = 50
        )
        self.tbl_cidades.column(
            "sigla",
            width = 20
        )
        self.tbl_cidades.heading(
            "id",
            text = "ID"
        )
        self.tbl_cidades.heading(
            "nome",
            text = "nome"
        )
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command= self.fechar
        )
        self.tbl_cidades.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cidade
        )
    def preencher_campos(self):
        
        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(Cidade.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_Nome.insert(
            0,
            Cidade.nome
        )

        self.txt_Sigla.insert(
            0,
            Cidade.Sigla
        )
    def limpar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_id_Nome.delete(0, tk.END)
        self.txt_id_Sigla.delete(0, tk.END)
    
    def get_id_selecionado(self):
        item = self.tbl_cidades.selection()[0]

        return self.tbl_cidades.item(item)["value"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta cidade ?"
        )

    def ler_dados_cidades(self):
        Nome = self.txt_Nome.get()
        Sigla = self.txt_Sigla.get()
        return Nome, Sigla
    
    def limpar_treeview(self):
        for item in self.tbl_cidades.get_children():
            self.tbl_cidades.delete(item)


    def exibir_mensagem(self, mensagem, sucesso = True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                   "Mini ERP",
                mensagem
            )

    def exibir_cidades(self, cidades):

        self.limpar_treeview()
        for cidades in cidades:
            self.tbl_cidades.insert(
                "",
                tk.END,
                values=(
                    cidades.id,
                    cidades.Nome,
                    cidades.Sigla
                )
            )


    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_cidades()
        self.controller.get_all()
        self.root.mainloop()