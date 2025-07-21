import streamlit as st
from datetime import date

from project_starter import init_database, OrchestratorAgent, db_engine

# Initialize database and orchestrator once
@st.cache_resource
def get_agent():
    init_database(db_engine)
    return OrchestratorAgent()

orch = get_agent()

st.title("Munder Difflin Quote Assistant")

request_text = st.text_area("Pedido do cliente")
request_date = st.date_input("Data do pedido", value=date.today())

if st.button("Enviar solicitação"):
    resp = orch.handle_request(request_text, request_date.strftime("%Y-%m-%d"))
    st.write(resp)
