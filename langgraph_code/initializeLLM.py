from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

def get_openai_llm():
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")
    return llm

def get_google_genai_llm():
    pass



if __name__ == "__main__":
    model = get_openai_llm()
    response = model.invoke("Hello, How are you?")
    print(response.content)
