from datetime import datetime

class Agendamento:
    def __init__(self, titulo, data_inicio, data_fim, local, atividades=None):
        self.titulo = titulo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.local = local
        self.atividades = atividades

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data):
        try:
            self._data_inicio = datetime.strptime(data, "%d-%m-%Y %H:%M")
        except ValueError as e:
            print(f"Formato de data de início inválido. Use 'dd-mm-aaaa HH:MM'. Erro: {e}")
            self._data_inicio = None

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, data):
        try:
            self._data_fim = datetime.strptime(data, "%d-%m-%Y %H:%M")
        except ValueError as e:
            print(f"Formato de data de fim inválido. Use 'dd-mm-aaaa HH:MM'. Erro: {e}")
            self._data_fim = None
    
    def __str__(self):
        return f"Agendamento cadastrado: {self.titulo} em {self.local}"

    def exibir_dados(self):
        txt = f"Agendamento cadastrado: {self.titulo}\n Local: {self.local}"
        
        dt_inicio = self.data_inicio.strftime('%d/%m/%Y às %H:%M') if self.data_inicio else "Não definida"
        dt_fim = self.data_fim.strftime('%d/%m/%Y às %H:%M') if self.data_fim else "Não definida"
        if (self.atividades is not None):
            txt += f"\n Atividades: {self.atividades}"
        txt += f"\n Início: {dt_inicio}\n Fim: {dt_fim}"

        return txt
    