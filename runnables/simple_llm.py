from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model =ChatOpenAI()

prompt= PromptTemplate(
    template='suggest a attention grabbing blog title about a {topic}',
    input_variables=['topic']
)
#define input
topic = input("enter topic \n")

#format prompt manually using prompttemplate
formated_prompt=prompt.format(topic=topic)

#call llm
blog_title=model.predict(formated_prompt)

print("generated blog title :",blog_title)