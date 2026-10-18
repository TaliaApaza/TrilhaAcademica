import time
import streamlit as st
from servicos.ServicoEntrega import *

class TelaEntregar():
    servico = None

    def __init__(self):
        self.servico = ServicoEntrega()

    def inicio_entrega(self):
        st.header("Tela de Entrega de tarefas")
        # Será simulado o usuário logado com o ID=1.
        aluno_id = 1
        disciplinas = self.servico.listar_disciplinas(aluno_id)
        tarefas = self.servico.tarefas_disponiveis(aluno_id)
        if tarefas:
            tarefa_selecionada = st.selectbox(
                "Escolha a tarefa que será entregue:",
                tarefas,
            )
        else:
            st.warning("Nãohátarefas para entregar.Parabéns!!!")
        disciplina_selecionada = st.selectbox(
            "Escolha a disciplina da tarefa:",
            disciplinas,
        )
        if tarefas and st.button("Registrar Entrega", type="primary"):
            self.clicar_entregar(tarefa_selecionada, disciplina_selecionada)

    def clicar_entregar(self, tarefa, disciplina):
        self.servico.emprestar(tarefa, disciplina)
        st.success("Entrega registrada com sucesso!!!")
        time.sleep(2)
        st.switch_page("index.py")

TelaEntregar().inicio_entrega()