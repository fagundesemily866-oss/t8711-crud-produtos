import os
from app.models.cidade import Cidade

class cidade_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view


    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            Nome, Sigla, = self.view.ler_dados_cidade()
            cidade = cidade(
                    None,
                    Nome, 
                    Sigla
                )
            self.dao.save(cidade)
            self.get_all()
            self.view.exibir_mensagem("Cidade cadastrada com sucesso!")
        except ValueError:
            self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
        
    def get_all(self):
        cidades = self.dao.get_all()
        self.view.exibir_cidades(cidades)

    def selecionar_cidade(self, event):
        try:
            id_cidade = self.view.get_id_selecionado()
            self.cidade_selecionada = self.dao.get_by_id(
                id_cidade
            )
            self.view.preencher_campos(
                self.cidade_selecionada
            )

        except IndexError:
            pass        
    def update(self):
        try:
            if self.cidade_selecionada is None:
                self.view.exibir_mensagem("Selecione uma cidade na lista.", False)
                return
            Nome, Sigla = self.view.ler_dados_cidade()
            self.cidade_selecionada.atualizar_dados(Nome, Sigla)
            self.dao.update(self.cidade_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Cidade atualizada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.cidade_selecionada is None:
            self.view.exibir_mensagem("Selecione uma cidade na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.cidade_selecionada.id)
            if sucesso:
                self.cidade_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Cidade excluída com sucesso!")
            else:
                self.view.exibir_mensagem("Cidade não encontrada.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir cidade", False)

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                self.save()
            
            elif opcao == 2:
                self.get_all()
            
            elif opcao == 3:
                self.update()
                
            elif opcao == 4:
                self.delete()
                
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
                
