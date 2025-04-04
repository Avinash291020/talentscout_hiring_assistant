import streamlit as st
from utils import initialize_session
from chatbot_logic import handle_input
from prompts import greeting_prompt
from datetime import datetime

st.set_page_config(page_title="TalentScout AI Hiring Assistant", layout="centered")
st.title("🤖 TalentScout Hiring Assistant")

# 🧠 Initialize session
initialize_session()

# 🧠 Start conversation if at greeting stage
if st.session_state.stage == "greeting":
    bot_response, next_stage = handle_input("", "greeting", st.session_state.user_data)
    st.session_state.chat_history.append(("bot", bot_response))
    st.session_state.stage = next_stage

# 💬 Chat History Display with styling
chat_container = st.container()
with chat_container:
    for role, message in st.session_state.chat_history:
        st.markdown(f"**{role.capitalize()}:** {message}")

# 📥 Input Form (placed BELOW messages)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="input")
    submitted = st.form_submit_button("Send")

    if submitted:
        if user_input:
            st.session_state.chat_history.append(("user", user_input))
            bot_response, next_stage = handle_input(user_input, st.session_state.stage, st.session_state.user_data)
            st.session_state.chat_history.append(("bot", bot_response))
            st.session_state.stage = next_stage
            st.rerun()

# 🧹 Clear Chat Button
if st.button("🧹 Clear Chat"):
    st.session_state.stage = "greeting"
    st.session_state.user_data = {}
    st.session_state.chat_history = []
    st.rerun()

# 👇 Auto-scroll to bottom using JavaScript
scroll_js = """
<script>
    var chat_container = window.parent.document.querySelector('.main');
    chat_container.scrollTo(0, chat_container.scrollHeight);
</script>
"""
st.components.v1.html(scroll_js, height=0)
