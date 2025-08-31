import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

conversation = []

def save_memory():
    """Save chat history to memory.json"""
    with open("memory.json", "w") as f:
        json.dump(conversation, f)

def load_memory():
    """Load chat history from memory.json"""
    global conversation
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            conversation = json.load(f)

def chat_loop():
    """Run chatbot in CLI"""
    print("Gemini Chatbot started (type 'exit' to quit)")
    load_memory()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            save_memory()
            print("Chat saved. Goodbye! 👋")
            break
        try:
            chat_text = ""
            for msg in conversation:
                chat_text += f"{msg['role']}: {msg['content']}\n"
            chat_text += f"User: {user_input}\n"

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(chat_text)
            reply = response.text

            print("Bot:", reply)

            conversation.append({"role": "user", "content": user_input})
            conversation.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_loop()
