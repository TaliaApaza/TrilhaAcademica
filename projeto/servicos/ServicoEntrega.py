from daos.DisciplinaDAO import *
from daos.EntregaDAO import *
from daos.TarefaDAO import *


class ServicoEntrega():
    dao_disciplinas = None
    dao_tarefas = None
    dao_entregas = None

    def __init__(self):
        self.dao_disciplinas = DisciplinaDAO()
        self.dao_tarefas = TarefaDAO()
        self.dao_entregas = EntregaDAO()

    def listar_disciplinas(self, usr_id):
        return self.dao_disciplinas.get_disciplinas(usr_id)

    def tarefas_disponiveis(self, usr_id):
        return self.dao_tarefas.get_disponiveis(usr_id)

    def entregar(self, tarefa, disciplina):
        self.dao_tarefas.marcar_indisponivel(tarefa)
        return self.dao_entregas.entregar(tarefa, disciplina)