from model.Tarefa import Tarefa
from model.TarefaProfissional import TarefaProfissional
from model.TarefaPessoal import TarefaPessoal
from model.Agendamento import Agendamento
from model.Compromisso import Compromisso

print("Tarefa Profissional:")
t1 = TarefaProfissional(
    nome_tarefa="Desenvolvimento de ferramenta",
    projeto="Projeto interno",
    data_entrega="05-12-2025",
    descricao="Desenvolver ferramenta para versionamento"
)
print(t1.exibir_dados())

print("\nTarefaPessoal:")
t2 = TarefaPessoal(
    nome_tarefa="Limpeza da casa",
    descricao="Limpar o banheiro",
    tipo="Doméstica",
    data_realizacao="07-10-2025"
)
print(t2.exibir_dados())

print("\nCompromisso: ")
c1 = Compromisso(
    nome_tarefa="Consulta Dentista",
    local="Clínica Borin",
    data_realizacao="06-10-2025",
    data_inicio="06-10-2025 13:00",
    data_fim="06-10-2025 14:30",
    descricao="Visita preventiva periódica",
    atividades="Análise bucal diagnóstica"
)
c1.concluir()
print(c1.exibir_dados())    

print("\nAgendamento:")
a1 = Agendamento(
    titulo="Consulta Dentista",
    local="Clínica Borin",
    atividades="Limpeza periódica e endodontia",
    data_inicio="07-10-2025 15:00",
    data_fim="07-10-2025 17:00"
)
print(a1.exibir_dados() + "\n")