from langchain_core.prompts import (HumanMessagePromptTemplate,
 SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
                                    )
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langgraph_code.initializeLLM import get_openai_llm

llm = get_openai_llm()
def get_session_history(session_id):
    return SQLChatMessageHistory(session_id,"sqlite:///chat_history.db")

system = SystemMessagePromptTemplate.from_template("You are helpful assistant.")
human = HumanMessagePromptTemplate.from_template("{input}")
messages = [system, MessagesPlaceholder(variable_name='history'), human]
prompt = ChatPromptTemplate(messages=messages)
chain = prompt | llm | StrOutputParser()
runnable_with_history = RunnableWithMessageHistory(chain, get_session_history,
                                                   input_messages_key='input',
                                                   history_messages_key='history')


def chat_with_llm(session_id, input):
    output = runnable_with_history.invoke(
        {'input': input},
        config={'configurable': {'session_id': session_id}}
    )
    return output

session_id='abc123'
about="Hello My name is Ashraf, I work in TCS as a Senior Engineer"
response=chat_with_llm(session_id=session_id,input=about)
print(response)
response=chat_with_llm(session_id=session_id,input="what is my name and where I work ?")
print(response)
response=chat_with_llm(session_id=session_id,input="what is my role ?")
print(response)