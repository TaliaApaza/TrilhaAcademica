from modelos.models import Aluno
from peewee import IntegrityError

class AlunoDAO:

    def cadastrar(self, login, senha):
        try:
            aluno = Aluno.create(login=login, senha=senha)
            return aluno

        except IntegrityError:
            print("Erro: não foi possível cadastrar o aluno.")
            return None