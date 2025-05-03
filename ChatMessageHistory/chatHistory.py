from setuptools.config.setupcfg import configuration_to_dict

from langgraph_code.initializeLLM import get_openai_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

llm = get_openai_llm()
template = PromptTemplate.from_template("{prompt}")
chain = template | llm | StrOutputParser()
about = "Where I work ?"
# response = chain.invoke({"prompt":about})
# print(response)

# response = chain.invoke({"prompt":"What is my name ?"})
# print(response)

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id,"sqlite:///chat_history.db")

runnable_with_history = RunnableWithMessageHistory(chain,get_session_history)

user_id = 'asharaf123'
history = get_session_history(user_id)
history.get_messages()
history.clear()

response = runnable_with_history.invoke([HumanMessage(content=about)],
                             config={'configurable' : {'session_id':user_id}}
                             )
print(response)


##################### Setting - Up History with MessagePlaceHolder #############
