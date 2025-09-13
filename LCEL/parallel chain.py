from langgraph_code.initializeLLM import get_openai_llm
from langchain_core.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
llm = get_openai_llm()

system_prompt = SystemMessagePromptTemplate.from_template("You are a {school} teacher, answer user query in {num} short sentences.")
human_prompt = HumanMessagePromptTemplate.from_template("Tell me about {topic}.")
messages = [system_prompt, human_prompt]
template = ChatPromptTemplate(messages)
about_chain = template | llm | StrOutputParser()



human_prompt_poem = HumanMessagePromptTemplate.from_template("Tell me a short poem on the {topic}.")
messages = [system_prompt, human_prompt]
template = ChatPromptTemplate(messages)
poem_chain = template | llm | StrOutputParser()

chain = RunnableParallel(about=about_chain,poem=poem_chain)
response = chain.invoke({"school":"elementary","num":3,"topic":"sun"})
print(response['about'],'\n\n',response['poem'])







