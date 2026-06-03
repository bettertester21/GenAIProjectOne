import os
from langchain_ollama import ChatOllama
import streamlit as st
st.title("LangChain Ollama :gemma3:1b Demo")
# Initialize the model
llm = ChatOllama(model="gemma3")
# User input
question = st.text_input("Enter Your Question:")
# Generate response
if question:
    response = llm.invoke(question)
    st.write("Response:", response.content)