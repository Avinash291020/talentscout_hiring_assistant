import re
import streamlit as st
from config import EXIT_KEYWORDS

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^[0-9\-\+\s]{10,15}$", phone)

def should_end_conversation(user_input):
    return any(word.lower() in user_input.lower() for word in EXIT_KEYWORDS)

def initialize_session():
    if 'stage' not in st.session_state:
        st.session_state.stage = 'greeting'
        st.session_state.user_data = {}
        st.session_state.chat_history = []
