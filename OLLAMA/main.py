from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
template = '''
answer the question below

here is the conversation history:{context}

Question:{question}

Answer: 
'''

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# for storing history
def handle_conv():
    context = ""
    print("welcome to the Raiden ai ! Type 'exit' to quit")
    while True:

        user_input = input("you: ")

        if user_input.lower() == "exit":
            break

# model = OllamaLLM(model="mistral")
# model = OllamaLLM(model="gemma:2b")
# result = model.invoke(input="hello world")
# result = chain.invoke({"context":"","question":"hi dude  "})
        result = chain.invoke({"context":context,"question":user_input})
        print("bot:", result)
        context+=f"\nUser:{user_input}\nRaiden:{result}"

if __name__ == "__main__":
    handle_conv()
