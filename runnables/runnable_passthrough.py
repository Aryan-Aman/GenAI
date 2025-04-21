from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# passsthrough = RunnablePassthrough()
# print(passsthrough.invoke({"topic": "cat"}))

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

generate_joke = RunnableSequence(prompt_1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explain": RunnableSequence(prompt_2, model, parser)
    }
)

final_chain = RunnableSequence(generate_joke, parallel_chain)
res= final_chain.invoke({"topic": "cat"})
print(res)
