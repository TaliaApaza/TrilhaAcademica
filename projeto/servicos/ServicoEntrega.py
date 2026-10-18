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

    def entregar(self, tarefa):
        self.dao_tarefas.marcar_indisponivel(tarefa)
        return self.dao_entregas.entregar(tarefa)

    def cancelar_entrega(self, entrega_id):
        try:
            self.dao_entregas.cancelar_entrega(entrega_id)
            return "Entrega cancelada com sucesso!"

        except Entrega.DoesNotExist:
            return "Erro: entrega não encontrada."
