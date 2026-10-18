from modelos.models import Disciplina

class DisciplinaDAO():

    def get_disciplinas(self, usr):
        return Disciplina.select().where(Disciplina.aluno == usr)
    
    def get_by_id(self, id_disciplina):
        return Disciplina.get_or_none(Disciplina.id == id_disciplina) 