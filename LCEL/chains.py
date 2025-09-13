from langgraph_code.initializeLLM import get_openai_llm
from langchain_core.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = get_openai_llm()

## Sequential Langchain expression language
system_prompt = SystemMessagePromptTemplate.from_template("You are a {school} teacher, answer user query in {num} short sentences.")
human_prompt = HumanMessagePromptTemplate.from_template("Tell me about {topic}.")
messages = [system_prompt, human_prompt]
template = ChatPromptTemplate(messages)
chain = template | llm | StrOutputParser()
response = chain.invoke({"school":'PhD',"num":3,"topic":"sun"})

### adding one sequential chain by using response from previous chain

analyse_prompt = ChatPromptTemplate.from_template("""You are a response analyzer, analyse the given {response} and
                                                     and tell me how difficult it is to understand in a sentence.
                                                     In addition to that you can also give me difficulty rating in a scale 
                                                     of 1 to 10.
                                                  """)

analyze_chain = analyse_prompt | llm | StrOutputParser()
analyzer_response = analyze_chain.invoke({"response":response})
print(analyzer_response)




