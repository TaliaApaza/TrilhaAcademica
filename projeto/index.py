import streamlit as st

##
## Definição das páginas e navegação
##
pages = {
    "Pessoal": [
        st.Page("pages/TelaPrincipal.py", title="Página Principal"),
        st.Page("pages/TelaEmprestimo.py", title="Tela de Empréstimo"),
    ],
    #"Recursos": [
        #st.Page("#", title="Sobre nós"),
        #st.Page("#", title="Inscreva-se"),
    #],
}
pg = st.navigation(pages)
pg.run()