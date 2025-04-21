from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt_1 = PromptTemplate(
    template = 'write a joke about a {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser =StrOutputParser()

prompt_2 = PromptTemplate(
    template = 'explain the joke briefly -{text}',
    input_variables = ['text']
)

chain = RunnableSequence(prompt_1, model, parser, prompt_2, model, parser)
print(chain.invoke({"topic": "cat"}))