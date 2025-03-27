#step1> take user prompt ;step 2 >send to llm ; step 3 > get structured output response
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='generate 5 interesting facts about {topic}',
    input_variables={'topic'},
)
model =ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'topic':'vibe coding'})

print(res)

chain.get_graph().print_ascii()