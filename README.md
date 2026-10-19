# Trilha Academica (Projeto APOO 2026)

Projeto desenvolvido, como exemplo, do contexto da disciplina de Análise e Projeto Orientado a Objetos com o objetivo de atividade academica.

# Responsáveis

1. Aluno. Juan Davi de Almeida Silva - Aluno do curso Informática Para Internet , no ano letivo de 2026

2. Aluna. Talia De Sousa Apaza - Aluna do curso Informática Para Internet no ano letivo de 2026

3. Aluno. Elverty Alberton Justino da Silva - Aluno de Informática Para Internet no ano letivo de 2026

4. Aluno. Jose Hiago Da Batista- Aluno de Informática Para Internet , no ano letivo de 2026

# Manipulação de Dados, Validações e Ciclo de Vida do Objeto

Foco: Operações CRUD clássicas, persistência do estado dos objetos e integridade de dados.

## Inserção de dados
**Processo de adicionar novas informações a um banco de dados.**

**1.Model.create():**
O método create() utilizado para criar e inserir um novo registro no banco de dados. Ele permite informar os valores dos campos do objeto diretamente no momento da criação. Ao executar create(), o Peewee executa uma operação de inserção(INSERT) no banco de dados. A chave primária da nova linha é recuperada automaticamente e armazenada na instância do modelo. Isso permite que o objeto criado tenha acesso ao identificador do registro inserido.

Exemplo:
aluno = Aluno.create(nome="Ana", idade=17)
print(aluno.id)

**2.Model.save():**
O método .save() é utilizado para persistir um objeto no banco de dados. Ele permite criar um registro ou salvar alterações em um objeto existente. Oferece mais controle sobre objeto antes de salvá-lo. Ele retorna a quantidade de linhas afetadas e é possível acessar sua chave primária por meio do atributo id.

Exemplo:
aluno = Aluno(nome="Carlos", idade=18)
aluno.save()
print(aluno.id)

**3.insert_many()**
A inserção em lote permite adicionar vários registros ao banco de dados de forma mais eficiente. Utilizar create() várias vezes é uma alternativa, mas pode apresentar desempenho inferior, já que cada chamada gera uma inserção individual.

O método insert_many() recebe uma lista de dicionários ou de tuplas e constrói uma consulta para inserir os registros. A execução ocorre quando chamamos execute().

Exemplo com dicionários:
A inserção em lote permite adicionar vários registros ao banco de dados de maneira eficiente. Utilizar create() repetidamente dentro de um laço é uma alternativa, mas pode apresentar desempenho inferior, já que cada chamada gera uma inserção individual.

O método insert_many() recebe uma lista de dicionários ou de tuplas e constrói uma consulta para inserir os registros. A execução ocorre quando chamamos execute().

Exemplo com dicionários:
alunos = [
    {"nome": "Maria", "idade": 16},
    {"nome": "João", "idade": 17},
    {"nome": "Beatriz", "idade": 18}
]
Aluno.insert_many(alunos).execute()

Exemplo com tuplas:
dados = [
    ("Luiza", 17),
    ("Pedro", 18)
]
Aluno.insert_many(
    dados,
    fields=[Aluno.nome, Aluno.idade]
).execute()

Quando usamos tuplas, precisamos informar os campos por meio do argumento fields, indicando a qual coluna corresponde cada posição da tupla.

## Leitura e busca de registros
**Processo de consultar informações que já estão armazenadas em um banco de dados.**

**1.get():**
Explicação

**2.get_or_none():**
Explicação

**3.get_or_create()**
Explicação

## Atualização e Remoção
**Operações utilizadas para modificar ou excluir informações que já estão armazenadas em um banco de dados.**

**1.save():**
Explicação

**2.update():**
Explicação

**3.execute():**
Explicação

**4.delete_instance()**
Explicação

## Sinais/Hooks do Peewee
**São mecanismos que permitem executar funções automaticamente quando determinadas operações acontecem em um modelo, como antes ou depois de salvar ou excluir um registro.**

**1.pre_save:**
Explicação

**2.post_save:**
Explicação

**3.pre_delete**
Explicação


# Documentação

Clique em cada um dos links abaixo para acessar o artefato específico.

1. [Documento de Visão](doc/visao/doc-visao.md)
1. [Modelo de Casos de Uso](doc/cdu/cdu.md)
1. [Modelo de Domínio](doc/dominio/dominio.md)
1. [Modelo de Dados](doc/bd/bd.md)
