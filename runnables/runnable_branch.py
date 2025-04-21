from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt_1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)
prompt_2= PromptTemplate(
    template='write a summary of the report - {text}',
    input_variables=['text']
)
model = ChatOpenAI()
parser = StrOutputParser()  

#sequential chain
# repo_gen_chain = RunnableSequence(prompt_1, model, parser) #parser > x 
repo_gen_chain = prompt_1 | model | parser  #LCEL

#send tuples in runnablebranch, no of conditions = no of tuples
branch_chain = RunnableBranch(
    # (lambda x: len(x.split())>500, RunnableSequence(prompt_2, model, parser)),
    (lambda x: len(x.split())>500, prompt_2 | model | parser), #lcel
    RunnablePassthrough() #default case, if no condition is met, it will pass the input as it is
)

final_chain = RunnableSequence(repo_gen_chain, branch_chain)
res = final_chain.invoke({"topic": "High frequency trading"})
print(res)
