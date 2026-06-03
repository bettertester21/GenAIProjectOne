# Name: 03_web_based_local_llama_chatbot.py
# Command to install streamlit library:  pip install streamlit 
# streamlit run 03_web_based_local_llama_chatbot.py
# Import necessary libraries
import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize the Ollama package with specified parameters so 
# it can use Meta's llama3 large language model
llm = OllamaLLM(model="llama3", temperature=0)

# Set up the title for the Streamlit app
st.title("Local Web-based Chatbot")

# Prompt the user to enter a question
user_input = st.text_input("Enter your question:")

# Display a button to execute the question
if st.button("Execute"):
    # Prepare the input prompt for the model by formatting the user's question
    prompt = [f"Prompt: {user_input}\nResponse:"]

    # Generate a response
    invoke_response = llm.invoke(prompt)

    # Display the response on the screen
    st.write(f"Response:\n{invoke_response}")

    # End - Python Program to create local chatbot
