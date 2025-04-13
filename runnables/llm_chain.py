#import openai, llmchain, prompttemplate
from langchain.llms import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


#Load llm
llm = openai(model_name="gpt-3.5-turbo", temperature=0.7)

#prompt template
prompt = PromptTemplate(
    template='suggest a attention grabbing blog title about a {topic}',
    input_variables=['topic']
)
#create llm chain
chain = LLMChain(llm = llm, prompt=prompt)

#run chain with specific topic
topic = input("enter topic")
output = chain.run(topic)

#output
print("generated blog title:", output)