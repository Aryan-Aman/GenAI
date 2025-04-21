from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='write a linkedin post about a {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write a tweet about a {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

#runnableparallel : initialized in a dict format
parallel_chain = RunnableParallel(
    {
        "linkedin": RunnableSequence(prompt1, model, parser),
        "tweet": RunnableSequence(prompt2, model, parser)
    }
)

res = parallel_chain.invoke({"topic": "Nifty50"})

print(res)
print(res['linkedin'])
print(res['tweet'])

