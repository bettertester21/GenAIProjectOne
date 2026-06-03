# Start - Python Program to Create Local Chatbot
# Name: 02_local_llama_chatbot.py 
# Command :  pip install langchain_ollama
# Import the Ollama class from the langchain_ollama module
from langchain_ollama import OllamaLLM

# Initialize the Ollama package with specified parameters so 
# it can use Meta's llama3 large language model
llm = OllamaLLM(model="llama3", temperature=0)

# Set up and print the title of the chatbot
print("Local Command-based ChatBOT")

# Prompt the user to enter a question
user_input = input("Enter your question: ")

# Prepare the input prompt for the model by formatting the user's question
prompt = [f"Prompt: {user_input}\nResponse:"]

# Generate a response 
invoke_response = llm.invoke(prompt)

# Display the generated response to the user
print(f"invoke_response_text:\n{invoke_response}")
# End - Python Program to create local chatbot
