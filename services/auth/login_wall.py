# services/auth/login_wall.py

import streamlit as st
from services.persistence.exercise_repository import get_or_create_user

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("🤖 AI Real-Time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start. 💪")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="unique name e.g. Kavya")
        submit_button = st.form_submit_button("Start session", use_container_width=True)
        
        if submit_button and username:
            # Get or create user and store ONLY the ID
            user = get_or_create_user(username)
            st.session_state.user_id = user['id']  # Store just the ID, not the whole row
            st.session_state.username = username
            st.rerun()
        elif submit_button:
            st.error("❌ Please enter a username")
    
    return False