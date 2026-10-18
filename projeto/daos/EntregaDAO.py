from modelos.models import Disciplina, Tarefa, Entrega

class EntregaDAO():

    def entregar(self, tarefa):
        entrega = Entrega(tarefa=tarefa)
        entrega.save()#save
        return entrega

    def cancelar_entrega(self, entrega_id):
        entrega = Entrega.get_by_id(entrega_id)

        tarefa = entrega.tarefa

        entrega.delete_instance()  #delete_instance()

        Tarefa.update(disponivel=True).where(
            Tarefa.id == tarefa.id
        ).execute() #update().execute()