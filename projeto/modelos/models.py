import datetime
from peewee import *

db = SqliteDatabase('trilha_academica.db')#cria banco de dados(trilha_academica)

class BaseModel(Model):#Herda a clase model do peewee 
    class Meta:
        database = db

## Classe ALUNO
####################
class Aluno(BaseModel):
    login = CharField(unique=True)
    senha = CharField()

    def set_login(self, login):
        if isinstance(login, str) and login.strip():
            self.login = login
        else:
            raise ValueError("Login deve ser uma string não vazia.")
    def set_senha(self, senha):
        if isinstance(senha, str) and senha.strip():
            self.senha = senha
        else:
            raise ValueError("Senha deve ser uma string não vazia.")

## Classe DISCIPLINA
##################
class Disciplina(BaseModel):
    nome = CharField(unique=True)
    professor = CharField()
    aluno = ForeignKeyField(Aluno, backref='disciplinas')

    def __str__(self):
        return f"({self.id}) {self.nome} {self.professor}"
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.nome = nome
        else:
            raise ValueError("Nome deve ser uma string não vazia.")
    def set_professor(self, professor):
        if isinstance(professor, str) and professor.strip():
            self.professor = professor
        else:
            raise ValueError("Professor deve ser uma string não vazia.")

## Classe TAREFA
##################
class Tarefa(BaseModel):
    titulo = CharField(unique=True)
    descricao = CharField()
    prazo = DateField()
    usuario = ForeignKeyField(Aluno, backref='tarefas')
    disciplina = ForeignKeyField(Disciplina, backref='tarefas')

    def __str__(self):
        return f"({self.id}) {self.titulo} {self.descricao}"
    def set_nome(self, titulo):
        if isinstance(titulo, str) and titulo.strip():
            self.titulo = titulo
        else:
            raise ValueError("Titulo deve ser uma string não vazia.")
    def set_descricao(self, descricao):
        if isinstance(descricao, str) and descricao.strip():
            self.descricao = descricao
        else:
            raise ValueError("Descriçao deve ser uma string não vazia.")
    def set_prazo(self, prazo):
        if isinstance(prazo, datetime.datetime):
            self.prazo = prazo
        else:
            raise ValueError("Prazo da Tarefa deve ser um objeto do tipo datetime.")

## Classe ENTREGA 
#######################
class Entrega(BaseModel):
    ativo = BooleanField(default=True)
    data_entrega = DateField(default=datetime.date.today)
    tarefa = ForeignKeyField(Tarefa, backref='emprestimos')

    def set_ativo(self, ativo):
        if isinstance(ativo, bool):
            self.ativo = ativo
        else:
            raise ValueError("Ativo deve ser um valor booleano.")
    def set_data_entrega(self, data_entrega):
        if isinstance(data_entrega, datetime.date):
            self.data_entrega = data_entrega
        else:
            raise ValueError("Data de Entrega deve ser um objeto do tipo date.")

def criar_tabelas():
    with db:
        db.create_tables([Aluno, Disciplina, Tarefa, Entrega])

def carga_inicial():
    # Criar um Aluno inicialaliea
    aluno = Aluno.create(login='teste', senha='senha123')

    # Criar algumas disciplinas iniciais
    disciplina1 = Disciplina.create(nome='Matematica', professor='Lucianjo', aluno=aluno)
    disciplina2 = Disciplina.create(nome='Português', professor='Fred', aluno=aluno)
   

    # Criar algumas tarefas iniciais
    #  iniciais
    tarefa = Tarefa.create(titulo='Redação', descricao = 'Escrever uma redação de 30 linha', prazo = datetime.date(2026/11/13), aluno=aluno)


if __name__ == '__main__':
    criar_tabelas()
    carga_inicial()