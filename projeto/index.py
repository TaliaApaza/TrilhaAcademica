import streamlit as st
from modelos.models import criar_tabelas

criar_tabelas()
##
## Definição das páginas e navegação
##
pages = {
    "Pessoal": [
        st.Page("pages/TelaPrincipal.py", title="Página Principal"),
        st.Page("pages/TelaEntregar.py", title="Tela de Entrega"),
    ]
}
pg = st.navigation(pages)
pg.run()