from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(model="llama3", temperature=0.7)

#Read input from user
input = input("Enter your question: ")
# Invoke the model
response = llm.invoke(input)
print(response)   
