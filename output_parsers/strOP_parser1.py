from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

# #1st prompt > deatailed report
template1 = PromptTemplate(
    template="Write a detailed summary on {topic}",
    input_variables=['topic']
)

#2nd prompt > summarize
template2 = PromptTemplate(
    template="Write a 5 line summary on following text. /n {text}",
    input_variables=['text']
)

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
res = chain.invoke({'topic': 'string theory'})
print(res)