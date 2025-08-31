## 📄 `README.md`

# 🤖 Gemini Conversational LLM

A conversational AI project built with **Python, Streamlit, and Google Gemini API**.  
The goal of this project is to demonstrate **prompt engineering fundamentals** and how the same Large Language Model (LLM) can behave differently when guided by **system prompts**.  

This was created as part of a Week 2 assignment: *"Building Your First Conversational LLM Interface"*.

---

## 📜 Project Details

### Objectives
- Build a functional conversational chatbot.  
- Show how **system prompts** can change the model’s tone and behavior.  
- Implement both **CLI** and **Web (Streamlit)** chat interfaces.  
- Demonstrate **conversation memory** and **error handling**.  

### Features
- ✅ **CLI Chatbot** with persistent memory (`memory.json`)  
- ✅ **Streamlit Web Interface** with chat bubbles and sidebar prompt selector  
- ✅ **3 Distinct Personalities** via system prompts:
  - **Professional Assistant** – formal, concise, business-like  
  - **Creative Companion** – imaginative, playful, poetic ✨  
  - **Technical Expert** – precise, detailed, scientific  
- ✅ Export chat history as JSON  
- ✅ Error handling for safe execution  
- ✅ Clear differences between response styles (assignment requirement)  

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Gemini-Conversational-LLM.git
cd Gemini-Conversational-LLM
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
```

Activate it:

* On Windows:

  ```bash
  .venv\Scripts\activate
  ```
* On Mac/Linux:

  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API Key

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Generate a **free Gemini API key**.
3. In the project folder, create a file named `.env`:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

⚠️ Do **not** commit `.env` to GitHub (it should be in `.gitignore`).

---

## ▶️ How to Run

### Run the CLI Chatbot

```bash
python cli_chat.py
```

* Type your questions directly in the terminal.
* Type `exit` to quit (chat history will be saved to `memory.json`).

### Run the Streamlit Web App

```bash
streamlit run streamlit_chat.py
```

* A browser window will open at `http://localhost:8501`.
* Use the sidebar to select **Professional / Creative / Technical** mode.
* Chat with different personalities.
* Use “Clear Chat” to reset or “Export Chat” to save the conversation.

---

## 🎯 Example Questions to Try

* “What is Artificial Intelligence?”
* “How do airplanes stay in the air?”
* “What happens inside a black hole?”
* “What is a Large Language Model (LLM)?”
* “What’s the best way to learn a new language?”

👉 Ask the same question in all three modes to see clear differences.

---

## 📸 Screenshots

*(Insert your CLI and Streamlit screenshots here before submission)*

---

## 📚 Reflection

This project gave me hands-on experience with **conversational AI** and **prompt engineering**.

* In **Part 1 (CLI chatbot)**, I learned how to use the Gemini API, manage conversation history, and implement error handling.
* In **Part 2 (System prompts)**, I discovered how strongly the **system role** affects responses. For example, the same question produced short formal bullet points in Professional mode, poetic answers with emojis in Creative mode, and precise scientific explanations in Technical mode.
* In **Part 3 (Streamlit interface)**, I learned how to turn a script into a simple, user-friendly web app with chat bubbles, sidebar controls, and export functionality.

Overall, this project showed me the importance of **prompt design**. Small changes in the system prompt can dramatically alter how the LLM communicates — making it formal, creative, or technical. I also gained experience in combining **APIs + Python + Streamlit** to build a working AI application.

---

## ⚠️ Notes

* Add `.env` to `.gitignore` to protect your API key.
* If you accidentally push your key, regenerate it from Google AI Studio.
* `memory.json` stores chat history locally but can be cleared anytime.

---

```

