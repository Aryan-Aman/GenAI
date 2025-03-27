from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt_1=PromptTemplate(
    template='generate a detailed report on {topic}',
    input_variables={'topic'}
)

prompt_2=PromptTemplate(
    template ='generate a 5 line summary pointwise(numbers) from the following text\n {text}',
    input_variables=['text']
)
model =ChatOpenAI()
parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

res = chain.invoke({'topic':'IRCTC'})
print(res)

chain.get_graph().print_ascii()