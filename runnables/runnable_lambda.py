from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt_1 = PromptTemplate(
    template = 'write a joke about a {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser =StrOutputParser()

joke_generator = RunnableSequence(prompt_1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        # "word_count": RunnableLambda(word_count)
        "word_count": RunnableLambda(lambda x: len(x.split()))
    }
)
final_chain = RunnableSequence(joke_generator, parallel_chain)

res= final_chain.invoke({"topic": "cat"})
final_res = """{}\n word count -{}""".format(res['joke'], res['word_count'])
print(final_res)