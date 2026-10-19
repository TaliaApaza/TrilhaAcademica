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

**2.Model.save():**
O método .save() é utilizado para persistir um objeto no banco de dados. Ele permite criar um registro ou salvar alterações em um objeto existente. Oferece mais controle sobre objeto antes de salvá-lo. Ele retorna a quantidade de linhas afetadas e é possível acessar sua chave primária por meio do atributo id.


**3.insert_many()**
A inserção em lote permite adicionar vários registros ao banco de dados de forma mais eficiente. Utilizar create() várias vezes é uma alternativa, mas pode apresentar desempenho inferior, já que cada chamada gera uma inserção individual.

O método insert_many() recebe uma lista de dicionários ou de tuplas e constrói uma consulta para inserir os registros. A execução ocorre quando chamamos execute().

Quando usamos tuplas, precisamos informar os campos por meio do argumento fields, indicando a qual coluna corresponde cada posição da tupla.

## Leitura e busca de registros
**Processo de consultar informações que já estão armazenadas em um banco de dados.**

**1.get():**
O método get() busca e recupera um único registro que corresponda às condições fornecidas na consulta. Quando ele encontra um registro, retorna uma instância do modelo. No entanto, caso nenhum registro corresponda às condições, responde com o tratamneot de exceção DoesNotExist. Esse método é indicado quando esperamos de fato encontrar determinado registro em vez de sua ausência.

**2.get_or_none():**
O método get_or_none() realiza uma busca muito semelhante à do get(). A principal diferença está no comportamento quando nenhum registro é encontrado. Enquanto o get() lança a exceção DoesNotExist, o get_or_none() retorna None. Isso facilita o tratamento de situações nas quais é possível que o registro pesquisado não exista. Portanto, o método é especialmente útil em consultas nas quais não há uma expectativa ou certeza da existência do registro.

**3.get_or_create()**
O método get_or_create() combina as operações de busca e criação de registros. Inicialmente, procura um objeto que corresponda aos critérios informados. Se não encontrar, cria um novo registro. Ele retorna dois valores: a instância encontrada ou criada e um booleano chamado *created*, que indica se ocorreu uma criação.

True: o registro foi criado.
False: o registro já existia.

**Argumento defaults**
O argumento defaults é utilizado com get_or_create() para definir valores que serão atribuídos aos campos caso um novo registro precise ser criado. Esses valores não participam dos critérios de busca. Caso o registro já exista, ele será retornado sem que os valores de defaults modifiquem seus atributos.

## Atualização e Remoção
**Operações utilizadas para modificar ou excluir informações que já estão armazenadas em um banco de dados.**

**1.save():**
É utilizado para obter um registro existente ou criar um novocaso não encontre nenhum que corresponda às condições fornecidas. Diferentemente dos dois métodos anteriores, ele reúne as operações de busca e criação em um único método. 
Quando a instância já representa um registro salvo e possui uma chave primária, uma nova chamada de save() normalmente executa uma operação SQL UPDATE, em vez de INSERT.
A chave primária do registro permanece a mesma.

**2.update().execute():**
Permite criar uma consulta para atualizar registros diretamente no banco de dados, sem precisar recuperar cada objeto individualmente. Apenas prepara a consulta.
Já o método execute() executa essa consulta e retorna a quantidade de linhas modificadas.
O método where() pode ser utilizado para determinar quais registros serão modificados.

**4.delete_instance()**
Permite excluir uma instância específica de um modelo. Normalmente, primeiro recuperamos o objeto utilizando get() e, em seguida, executamos a exclusão.
O método retorna a quantidade de linhas excluídas e disponibiliza parâmetros adicionais para controlar a remoção de registros relacionados.

recursive=True: permite excluir registros dependentes relacionados, de acordo com as relações entre os modelos.
delete_nullable: controla o comportamento da exclusão em relacionamentos cujas chaves estrangeiras permitem valores nulos.

## Sinais/Hooks do Peewee
**São mecanismos que permitem executar funções automaticamente quando determinadas operações acontecem em um modelo, como antes ou depois de salvar ou excluir um registro.**

**1.pre_save:**
É chamado imediatamente antes de um objeto ser salvo no banco de dados. Recebe o argumento *created*, que indica se o objeto está sendo criado pela primeira vez ou atualizado.

**2.post_save:**
É chamado imediatamente depois que um objeto é salvo no banco de dados. Também recebe o argumento *created*, permitindo identificar se ocorreu uma criação ou atualização.

**3.pre_delete**
É chamado imediatamente antes de um objeto ser excluído do banco de dados, quando se utiliza o método Model.delete_instance().


# Documentação

Clique em cada um dos links abaixo para acessar o artefato específico.

1. [Documento de Visão](doc/visao/doc-visao.md)
1. [Modelo de Casos de Uso](doc/cdu/cdu.md)
1. [Modelo de Domínio](doc/dominio/dominio.md)
1. [Modelo de Dados](doc/bd/bd.md)
