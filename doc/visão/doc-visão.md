# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :---: | :---: | :---: | :---: |
| 07/01/2026 | 0.1 | Versão inicial | Professor |
| - | - | - |  - |


## 1. Visão Geral do Sistema Proposto

O sistema tem por objetivo gerenciar o acervo de livros de um dado usuário, permitindo que este usuário possa registar o empréstimo e a devolução de livros específicos para algum dos seus amigos cadastrados no sistema.

## 2. Descrição do Problema
| - | - |
| :-: | :-: |
| **Problema** | Gerência do acervo pessoal de livros de um usuário |
| **Afeta** | O usuário |  
| **Impacta** | Ele pode esquecer para quem emprestou os seus livros |
| **Solução** | Gerenciar o empréstimo de livros para os amigos do usuário, bem como suas devoluções | 

## 3. Descrição dos Usuários 

| Usuário | Descrição | Responsabilidades |
| :---: | :---: | :---: |
| Usuário | Qualquer usuário que se cadastre no sistema | Manter o cadastro dos seus livros e amigos, registrar o empréstimo de livros, bem como suas devoluções |
| Administrador | Usuário que mantém o sistema | Tem prerrogativa de acessar e alterar todas as informações do sistema |

## 4. Descrição do Ambiente dos Usuários

| Usuário | Ambiente operacional |
| :---: | :---: |
| Usuário | computador desktop, com acesso à Internet |
| Administrador | computador desktop, com acesso à Internet |

## 5. Principais Necessidades dos Usuários

> Apresentadas no formato de tópicos
1. **Usuário**
   - Manter os cadastros dos seus livros e seus amigos
   - Registrar o empréstimo de um dado livro
   - Registrar a devolvução de um dado livro


## 6. Alternativas Concorrentes

1. **Skoob**
   - A maior plataforma brasileira do segmento. Permite catalogar os livros que você possui na estante física, registrar status de leitura (Lendo, Lido, Quero Ler, Relendo, Tenho), fazer resenhas, dar notas e controlar trocas de livros entre usuários.
   - LINK: https://www.skoob.com.br/
1. **Goodreads**
   - A maior plataforma mundial (pertencente à Amazon). É a principal referência de mercado para estantes virtuais, histórico de leitura, metas anuais e recomendações baseadas no acervo do usuário.
   LINK: https://www.goodreads.com
1. **BookBuddy**
   - Aplicativo focado na organização prática de bibliotecas físicas domésticas. Destaca-se pelo escaneamento de código de barras (ISBN) pela câmera do celular e pelo módulo de controle de empréstimos de livros para amigos.
   LINK: https://www.bookbuddyapp.com

## 7. Regras de Negócio

| ID  | Regra | Descrição |
| :--: | :--: | :--: |
| RN01 | Contato dos amigos | Todo amigo cadastrado no sistema necessariamente precisa ter pelo menos uma forma de contato |
| RN02 | Informações mínimas | Ao cadastrar um livro, ao menos necessita informar o nome do livro |

## 8. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :--: | :--: | :--: | :--: |
| RF01 | Cadastro de livros e amigos | Permite que o usuário cataloque seus livros e seus amigos | média |
| RF02 | Gerenciar o empréstimo de livros | Permite registrar que livros específicos sejam emprestados para um amigo, bem como suas devoluções | alta |


> **Prioridade**: alta, média ou baixa

## 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :--: | :--: | :--: | :--: | :--: |
| NF01 | Utilizar o Streamlit | Possibilitar que a aplicação execute com o suporte da plataforma Streamlit | implementação | obrigatório |
| NF02 | Utilizar um ORM | Possibilitar que a persistência de dados seja realizada através de um mecanismo de mapeamento objeto-relacional | implementação | obrigatório |

> **Categoria**: usabilidade, confiabilidade, performance, suportabilidade, restrição de projeto, implementação, interface e requisito físico - segundo classificação [FURP+](https://pt.wikipedia.org/wiki/FURPS).

> **Classificação**: desejável ou obrigatório.