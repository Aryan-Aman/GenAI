from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model =ChatOpenAI()

parser_1=StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['Positive', 'Negative']=Field(description='Give the sentiment of feedback')

parser_2 =PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='classify the sentiment of following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser_2.get_format_instructions()}
)

prompt_2=PromptTemplate(
    template='give an appropriate response to this positive feedback\n {feedback}',
    input_variables=['feedback']
)
prompt_3=PromptTemplate(
    template='give an appropriate response to this negative feedback\n {feedback}',
    input_variables=['feedback']
)
#classification chain +/-
classification_chain=prompt1 | model | parser_2

# res = classification_chain.invoke({'feedback':'this is a bad laptop'}).sentiment

branch_chain =RunnableBranch(
    (lambda x : x.sentiment =='positive', prompt_2 | model | parser_1),
    (lambda x : x.sentiment =='negative', prompt_3 | model | parser_2),
    RunnableLambda(lambda x : "could not find sentiment")

)

final_chain = classification_chain | branch_chain
# res = final_chain.invoke({'feedback':'this is a terrible phone'})
print(final_chain.invoke({'feedback':'this is a terrible phone'}))
final_chain.get_graph().print_ascii()