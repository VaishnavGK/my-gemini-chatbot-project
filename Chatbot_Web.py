import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

try:
    api_key=st.secrets["GEMINI_API_KEY"]
except (KeyError,FileNotFoundError):
    api_key=os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please set it in Streamlit secrets or in a local .env file.")



def get_gemini_model():
    return genai.GenerativeModel('gemini-1.5-flash-latest')


def get_gemini_response(model,prompt):
    try:
        response=model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred:{e}")
        return None

#TITLE
st.title("🤖 My Personal Gemini Chatbot")
st.caption("Web Interface for my first Chat bot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

model=get_gemini_model()

for message in st.session_state.chat_history:
    if message["role"]=="user":
        avatar="👤" 
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])
    

user_prompt=st.chat_input("Ask me anything...")

if user_prompt:
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
    with st.chat_message("user",avatar="👤"):
        st.markdown(user_prompt)
    

    if model:
        with st.spinner("Thinking..."):
            response_text=get_gemini_response(model, user_prompt)
            if response_text:
                st.session_state.chat_history.append({"role":"assistant","content":response_text})
                with st.chat_message("assistant"):
                    st.markdown(response_text)
