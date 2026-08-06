from app.models.estado import Estado

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Estado_View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Estados")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
  

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Estados",
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
            text = "Dados do Estado"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_Nome= tk.Label(
            self.frm_dados,
            text = "Nome:"
        )
        self.lbl_Nome.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_Nome = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_Nome.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_Sigla = tk.Label(
            self.frm_dados,
            text = "Sigla:"
        )
        self.lbl_.grid(
            row = 1,
            column = 0,
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
            column = 1,
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
        self.tbl_Estado = ttk.Treeview(
            self.root,
            height = 10
        )    
        self.tbl_Estado.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )  


    def configurar_treeview(self):
        self.tbl_Estado["columns"] = (
            "Nome",
            "Sigla"
            
        )
        self.tbl_Estado.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_Estado.column(
            "Nome",
            width =10
        )
        self.tbl_Estado.column(
            "Sigla",
            width = 50
        )
        self.tbl_Estado.heading(
            "Nome",
            text = "Nome"
        )
        self.tbl_Estado.heading(
            "Razao Social",
            text = "Razao Social"
        )
        self.tbl_fornecedores.heading(
            "cnpj",
            text = "CNPJ"
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
        self.tbl_fornecedores.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_fornecedor
        )
    def preencher_campos(self):
        
        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(Fornecedor.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_razao_social.insert(
            0,
            Fornecedor.razao_social
        )

        self.txt_nome_fantasia.insert(
            0,
            Fornecedor.nome_fantasia
        )

        self.txt_cnpj.insert(
            0,
            Fornecedor.cnpj
        )

        self.txt_sla.insert(
            0,
            str(Fornecedor.sla_atendimento)
        ) 

    def limpar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_id_Razao_Social.delete(0, tk.END)
        self.txt_id_nome_fantasia.delete(0, tk.END)
        self.txt_id_cnpj.delete(0, tk.END)
        self.txt_id_sla_.delete(0, tk.END)

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este Estado?"
        )

    def ler_dados_Estado(self):
        Nome = self.txt_Nome.get()
        Sigla = self.txt_Sigla.get()
        return Nome, Sigla
    
    def limpar_treeview(self):
        for item in self.tbl_Estado.get_children():
            self.tbl_Estado.delete(item)


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

    def exibir_Estados(self, Estado):

        self.limpar_treeview()
        for Estado in Estado:
            self.tbl_Estado.insert(
                "",
                tk.END,
                values=(
                    Estado.Nome,
                    Estado.Sigla
                    
                )
            )


    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_fornecedores()
        self.controller.get_all()
        self.root.mainloop()