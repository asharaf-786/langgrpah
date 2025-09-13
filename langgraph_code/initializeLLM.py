from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 
from langchain_ollama import ChatOllama

load_dotenv()

def get_openai_llm():
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")
    return llm

def get_ollama_llm():
    llm = ChatOllama(
        base_url="http://localhost:11434", 
        model="llama3.2:latest"
    )
    return llm

def get_ollama_embedding():
    from langchain_ollama import OllamaEmbeddings
    embedding = OllamaEmbeddings(
        base_url="http://localhost:11434", 
        model="nomic-embed-text:latest"
    )
    return embedding

if __name__ == "__main__":
    # model = get_openai_llm()
    # print(get_ollama_llm())
    get_ollama_embedding()
    # response = model.invoke("Hello, How are you?")
    # print(response.content)
