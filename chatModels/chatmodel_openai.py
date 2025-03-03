from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
'''temperrature=0 : same given input nearly same output everytime, if 1.5-2 different creative output everytime'''
model = ChatOpenAI(model='gpt-4', temperature=1.5)

result = model.invoke('write a 5 line poem on cricket')
print(result.content)

