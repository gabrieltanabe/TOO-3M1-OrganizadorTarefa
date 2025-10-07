from .Tarefa import Tarefa
from .Agendamento import Agendamento

class Compromisso(Tarefa, Agendamento):
    def __init__(self, nome_tarefa, data_realizacao, data_inicio, data_fim, local, descricao=None, atividades=None):
        
        Tarefa.__init__(self, nome_tarefa, descricao, data_realizacao)
        Agendamento.__init__(self, nome_tarefa, data_inicio, data_fim, local, atividades)

    def __str__(self):
        return f"[Compromisso] {self.nome} em {self.local}"

    def exibir_dados(self):
        return Tarefa.exibir_dados(self) + "\n" + Agendamento.exibir_dados(self)