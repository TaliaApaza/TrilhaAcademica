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
É utilizado para buscar e recuperar um único registro que corresponda às condições informadas na consulta.
Ele recebe filtros que determinam qual registro deve ser encontrado. Caso nenhum registro corresponda aos filtros, o método gera uma exceção chamada DoesNotExist.

**2.get_or_none():**
Realiza uma busca semelhante à do método get(), mas apresenta uma diferença importante: quando nenhum registro corresponde aos filtros informados, ele retorna None em vez de gerar uma exceção de registro não encontrado.

**3.get_or_create()**
É utilizado para obter um registro existente ou criar um novo
caso não encontre nenhum que corresponda às condições
fornecidas. Diferentemente dos dois métodos anteriores, ele reúne as operações de busca e criação em um único método.

## Atualização e Remoção
**Operações utilizadas para modificar ou excluir informações que já estão armazenadas em um banco de dados.**

**1.save():**
É utilizado para obter um registro existente ou criar um novo
caso não encontre nenhum que corresponda às condições fornecidas.
Diferentemente dos dois métodos anteriores, ele reúne as operações de busca e criação em um único método.

**2.update():**
Permite criar uma consulta para atualizar vários registros de uma só vez. Já o método execute() executa essa consulta e
retorna a quantidade de linhas modificadas.

**3.execute():**
Permite excluir uma instância específica de um modelo, ou seja, o documento apresenta parâmetros que permitem controlar a remoção de uma instância e de seus relacionamentos.


**4.delete_instance()**
Explicação

## Sinais/Hooks do Peewee
**São mecanismos que permitem executar funções automaticamente quando determinadas operações acontecem em um modelo, como antes ou depois de salvar ou excluir um registro.**

**1.pre_save:**
É chamado imediatamente antes de um objeto ser salvo no banco de dados. Recebe o argumento created, que indica se o objeto está sendo criado pela primeira vez ou atualizado.

**2.post_save:**
É chamado imediatamente depois que um objeto é salvo no banco de dados. Também recebe o argumento created, permitindo identificar se ocorreu uma criação ou atualização.


**3.pre_delete**
chamado imediatamente antes de um objeto ser excluído do banco de dados, quando se utiliza o método Model.delete_instance().


# Documentação

Clique em cada um dos links abaixo para acessar o artefato específico.

1. [Documento de Visão](doc/visao/doc-visao.md)
1. [Modelo de Casos de Uso](doc/cdu/cdu.md)
1. [Modelo de Domínio](doc/dominio/dominio.md)
1. [Modelo de Dados](doc/bd/bd.md)
