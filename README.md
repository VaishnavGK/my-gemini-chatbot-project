# 🤖 Gemini Chatbot with Streamlit

This is a simple web application built with Python and Streamlit that provides an interactive chat interface for Google's Gemini 1.5 Flash model. The app securely manages API keys and remembers conversation history for a natural, multi-turn dialogue.

## ✨ Features

- Interactive Chat UI: A clean and responsive user interface for chatting.
- Conversation History: The app stores the session's chat history, allowing for context-aware, follow-up questions.
- Secure API Key Handling: Uses a .env file to keep your Google AI API key safe and private.
- Error Handling: Gracefully warns the user if the API key is not configured.
- Efficient Model: Powered by the fast and capable gemini-1.5-flash-latest model.

---

## 🛠️ Setup & Installation

Follow these steps to run the project locally.

### Prerequisites

- Python 3.8+
- A Google AI API Key. You can obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation Guide

1.  Clone the repository:
   Bash:
    git clone [https://github.com/VaishnavGK/my-gemini-chatbot-project.git](https://github.com/VaishnavGK/my-gemini-chatbot-project.git)
    cd my-gemini-chatbot-project
    
2.  Install the required dependencies:
   
Bash:
    pip install -r requirements.txt
    
3.  Create an environment file:
    Create a new file named .env in the root of your project folder.

4.  Add your API key:
    Open the .env file and add your Google AI API key as follows:
   
shell:
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    
---

## 🚀 Usage

To run the application, execute the following command in your terminal from the project's root directory:
bash:
streamlit run Chatbot_Web.py
