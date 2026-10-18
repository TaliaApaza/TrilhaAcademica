import streamlit as st

class TelaPrincipal():

    def main(self):
        st.title("Aplicação - Trilha Academica")
        if st.button("Registrar entrega de tarefas", type="primary"):
            st.switch_page("pages/TelaEntregar.py")

TelaPrincipal().main()