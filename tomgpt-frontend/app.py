# app.py

import streamlit as st
from api import start_chat, continue_chat, get_chat

st.set_page_config(page_title="TomGPT", layout="centered")
st.title("TomGPT - Chat with AI")

# Input token (paste manually)
token = st.text_input("Paste your Google ID Token", type="password")

if token:
    # Show start new chat if not started
    if "chat_id" not in st.session_state:
        user_input = st.text_area("Start a new chat:")
        if st.button("Send") and user_input:
            reply = start_chat(token, user_input)
            st.session_state.chat_id = reply["chat_id"]
            st.session_state.history = [
                {"role": "user", "text": user_input},
                {"role": "assistant", "text": reply["reply"]},
            ]

    # Show ongoing chat
    else:
        st.subheader("Chat")
        for msg in st.session_state.history:
            st.markdown(f"**{msg['role'].capitalize()}**: {msg['text']}")

        user_msg = st.text_area("Your message:")
        if st.button("Continue") and user_msg:
            reply = continue_chat(token, st.session_state.chat_id, user_msg)
            st.session_state.history.append({"role": "user", "text": user_msg})
            st.session_state.history.append({"role": "assistant", "text": reply["reply"]})

        # Option to refresh full chat
        if st.button("Load Full Chat"):
            chat = get_chat(token, st.session_state.chat_id)
            st.session_state.history = [
                {"role": msg["role"], "text": msg["content"]} for msg in chat["messages"]
            ]
