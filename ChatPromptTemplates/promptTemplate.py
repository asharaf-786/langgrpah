from langgraph_code.initializeLLM import get_openai_llm
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate, PromptTemplate,ChatPromptTemplate

llm = get_openai_llm()
query = "Tell me about sun in 2 points"
response = llm.invoke(query)
print(response.content)

system = SystemMessage(content="You are a helpful assistant, answer uer query in PhD teacher style")
human = HumanMessage(content="Tell me about earth in 3 points in short sentences")
messages = [system, human]
response  = llm.invoke(messages)
print(response.content)

### Langchain Prompt Template ###

system_prompt = SystemMessagePromptTemplate.from_template("You are a {school} teacher, answer user query in {num} short sentences.")
human_prompt = HumanMessagePromptTemplate.from_template("Tell me about {topic}.")

# system_prompt.format(school='PhD',num=5)
# human_prompt.format(topic='sun')
messages = [system_prompt, human_prompt]
template = ChatPromptTemplate(messages)
question = template.invoke({"school":'elementary',"num":5,"topic":"sun"})
response = llm.invoke(question)
print(response.content)











