from .Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, nome_tarefa, tipo, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.tipo = tipo
        
    def __str__(self):
        return f"[Tarefa Pessoal] {super().__str__()}"

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo): 
        self.__tipo = tipo    
        
    def exibir_dados(self):
        return super().exibir_dados() + f"\n Tipo: {self.tipo}"