from modelos.models import Tarefa

class TarefaDAO():

    def get_disponiveis(self, usr):
        return Tarefa.select().where((Tarefa.aluno == usr) & (Tarefa.disponivel == True))

    def marcar_indisponivel(self, tarefa):
        tarefa.disponivel = False
        tarefa.save()#save

    def get_by_id(self, id_tarefa):
        return Tarefa.get_or_none(Tarefa.id == id_tarefa)