import streamlit as st
from rag_pipeline import create_rag

st.set_page_config(page_title="ServerBasket AI", layout="centered")

st.title("🛒 ServerBasket AI Assistant")
st.markdown("### 🤖 Your Smart Hosting & Server Advisor")

# Load model
@st.cache_resource
def load_qa():
    return create_rag()

qa = load_qa()

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = qa(user_input)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})