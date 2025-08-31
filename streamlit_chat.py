import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    return []

def save_memory(conversation):
    with open("memory.json", "w") as f:
        json.dump(conversation, f)

st.set_page_config(page_title="Gemini Chat", page_icon="🤖", layout="centered")
st.markdown("<h1 style='text-align: center;'>🤖 Gemini Conversational LLM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Experiment with system prompts and see how responses change</p>", unsafe_allow_html=True)

st.sidebar.header("⚙ Settings")
mode = st.sidebar.radio("Choose System Prompt Style:", ["professional", "creative", "technical"])
st.sidebar.info(f"Current Style: *{mode.capitalize()}*")

if "conversation" not in st.session_state:
    st.session_state.conversation = load_memory() or []
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:
    st.session_state.current_mode = mode
    st.session_state.conversation.append({"role": "system", "content": f"Mode selected: {mode.capitalize()}"})

if not any(msg["role"] == "system" for msg in st.session_state.conversation):
    st.session_state.conversation.insert(0, {"role": "system", "content": f"Mode selected: {mode.capitalize()}"})

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.conversation = [{"role": "system", "content": f"Mode selected: {mode.capitalize()}"}]

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.conversation.append({"role": "user", "content": user_input})
    try:
        chat_text = f"System: {SYSTEM_PROMPTS[mode]}\n"
        for msg in st.session_state.conversation:
            if msg["role"] != "system":
                chat_text += f"{msg['role'].capitalize()}: {msg['content']}\n"

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(chat_text)
        reply = response.text
        st.session_state.conversation.append({"role": "assistant", "content": reply})
    except Exception as e:
        reply = f"Error: {e}"
        st.session_state.conversation.append({"role": "assistant", "content": reply})

for msg in st.session_state.conversation:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(
                f"<div style='background-color:#DCF8C6; color:black; padding:10px; border-radius:10px;'>{msg['content']}</div>",
                unsafe_allow_html=True
            )
    elif msg["role"] == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(
                f"<div style='background-color:#2C2C2C; color:white; padding:10px; border-radius:10px;'>{msg['content']}</div>",
                unsafe_allow_html=True
            )
    elif msg["role"] == "system":
        with st.chat_message("system", avatar="⚙"):
            st.markdown(
                f"<div style='background-color:#E0E0E0; color:#333; padding:8px; border-radius:8px; font-style:italic;'>{msg['content']}</div>",
                unsafe_allow_html=True
            )

save_memory(st.session_state.conversation)

chat_text_export = f"System Mode Selected: {st.session_state.current_mode.capitalize()}\n\n"
for m in st.session_state.conversation:
    if m["role"] != "system":
        chat_text_export += f"{m['role'].capitalize()}: {m['content']}\n\n"

st.sidebar.download_button(
    "⬇ Export Chat ",
    data=chat_text_export,
    file_name="chat_history.txt",
    mime="text/plain"
)