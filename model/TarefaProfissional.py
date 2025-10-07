from datetime import datetime
from .Tarefa import Tarefa

class TarefaProfissional(Tarefa):
    def __init__(self, nome_tarefa, projeto, data_entrega, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.projeto = projeto
        self.data_entrega = data_entrega

    @property
    def data_entrega(self):
        return self._data_entrega

    @data_entrega.setter
    def data_entrega(self, data):
        try:
            self._data_entrega = datetime.strptime(data, "%d-%m-%Y")
        except ValueError as e:
            print(f"Formato de data de entrega inválido. Use 'dd-mm-aaaa'. Erro: {e}")
            self._data_entrega = None

    def __str__(self):
        return f"[Tarefa Profissional] {super().__str__()}"

    def exibir_dados(self):
        data_entrega = self.data_entrega.strftime('%d/%m/%Y') if self.data_entrega else "Não definida"
        return super().exibir_dados() + f"\n Projeto: {self.projeto}" + f"\n Data de Entrega: {data_entrega}"