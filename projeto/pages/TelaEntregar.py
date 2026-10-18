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
            st.warning("Não há tarefas para entregar.Parabéns!!!")
        if tarefas and st.button("Registrar Entrega", type="primary"):
            self.clicar_entregar(tarefa_selecionada)

    def clicar_entregar(self, tarefa):
        self.servico.entregar(tarefa)
        st.success("Entrega registrada com sucesso!!!")
        time.sleep(2)
        st.rerun()

TelaEntregar().inicio_entrega()