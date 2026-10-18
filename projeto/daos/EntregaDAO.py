from modelos.models import Disciplina, Tarefa, Entrega

class EntregaDAO():

    def entregar(self, tarefa, disciplina):
        entrega = Entrega(tarefa=tarefa, disciplina=disciplina)
        entrega.save()#save
        return entrega