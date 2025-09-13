from langgraph_code.initializeLLM import get_openai_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

llm = get_openai_llm()
prompt = PromptTemplate.from_template("""
                                     Given the user review , classify it as either being at Positive or Negative.
                                     Don't reply with more than one word. 
                                     Review : {review}
                                     Classification : 
                                     """)
chain = prompt | llm  | StrOutputParser()
# review = "I'm very happy that , it helped me to gain knowledge"
# response = chain.invoke({"review":'Positive Review'})
# print(response)

positive_prompt = PromptTemplate.from_template("""
         You are expert in writing reply for positive review.
         You need to encourage user to write their experience on social media.
         Review : {review}
         Answer :  """)
positive_chain = positive_prompt | llm | StrOutputParser()

negative_prompt = PromptTemplate.from_template("""
         You are expert in writing reply for negative review.
         You need to first apologies to user for the inconvenience caused.
         You need to ask user to share their concern on following email:'asharaf23@gmail.com'
         Review : {review}
         Answer :  """)
negative_chain = negative_prompt | llm | StrOutputParser()

def route(info):
    if 'positive' in info['sentiment'].lower():
        return positive_chain
    else:
        return negative_chain


full_chain = {"sentiment": chain, 'review': lambda x: x['review']} | RunnableLambda(route)

# review = "I'm very happy to say that this course taught me a lot."
review = "I'm not happy with the services you offered to me"
response = full_chain.invoke({"review":review})
print(response)
