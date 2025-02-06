import streamlit as st
import create
st.set_page_config(page_title="Head", page_icon="😀", layout="wide")

st.markdown("<h1 style='text-align: center;'>Autism Cure-inator</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_chatbot_response(message):
    

    return create.chatbot_response(message)

def send_message():
    if st.session_state.msg:
        st.session_state.chat_history.append(f"**User:** {st.session_state.msg}")
        response = get_chatbot_response(st.session_state.msg)
        st.session_state.chat_history.append(f"**{response}**")
        st.session_state.msg = ""

with st.container():
    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            st.markdown(message)
    else:
        st.markdown("_No messages yet. Start the conversation below!_")

c1, c2 = st.columns([10, 1], gap="small")

with c1:
    st.text_input("Message", placeholder="Enter a message", key="msg", label_visibility="collapsed",on_change=send_message)

with c2:
    st.button("Send", use_container_width=True, on_click=send_message)
