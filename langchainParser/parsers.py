from langgraph_code.initializeLLM import get_openai_llm
from pydantic import BaseModel,Field
from typing import Optional
from langchain_core.output_parsers import PydanticOutputParser,JsonOutputParser
from langchain.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser
llm = get_openai_llm()

class Joke(BaseModel):
    setup:str = Field(description="the description of the joke")
    punchline:str = Field(description="the punchline of the joke")
    rating:Optional[int] = Field(description="the rating of the joke from 1 to 10")

parser = PydanticOutputParser(pydantic_object=Joke)
instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template =  """Answer the user query with a joke, here is your formatting instruction.
     {format_instructions}
     Query : {query}
     """,
     input_variables = ['query'],
     partial_variables = {"format_instructions":instructions}
)

chain = prompt | llm | parser
response = chain.invoke({"query":"tell me a joke about Men"})
print(response)


#### With Structure Output

class Fact(BaseModel):
    fact:str = Field(description="the fact about the given topic")
    interesting:str = Field(description="the interesting thing about the given topic")

prompt = PromptTemplate.from_template("""
Given the user query, answer with the fact as well as the interesting thing about the given topic.
Query : {query}
Answer : 
""")
fact_chain = prompt | llm.with_structured_output(Fact)
response = fact_chain.invoke({"query":"tell me about Men"})
print(response)


### JsonOutputParser


parser = JsonOutputParser(pydantic_object=Joke)
instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template =  """Answer the user query with a joke, here is your formatting instruction.
     {format_instructions}
     Query : {query}
     """,
     input_variables = ['query'],
     partial_variables = {"format_instructions":instructions}
)
chain = prompt | llm | parser

response = chain.invoke({"query":"tell me a joke about Women"})
print(response)



####DatetimeOutput Parser


parser = DatetimeOutputParser()
instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template =  """Answer the user query with a joke, here is your formatting instruction.
     {format_instructions}
     Query : {query}
     """,
     input_variables = ['query'],
     partial_variables = {"format_instructions":instructions}
)
chain = prompt | llm | parser
response = chain.invoke({"query":"When india beat China in terms of population ?"})
print(response)



