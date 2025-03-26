from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

# Llm= HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )
model = ChatOpenAI()
# model = ChatHuggingFace(llm=Llm)

# #1st prompt > deatailed report
template1 = PromptTemplate(
    template="Write a detailed summary on {topic}",
    input_variables=['topic']
)

#2nd prompt > summarize
template2 = PromptTemplate(
    template="Write a 4 line summary on following text. /n {text}",
    input_variables=['text']
)

prompt_1 = template1.invoke({'topic':'black hole'})
res_1 = model.invoke(prompt_1)

prompt_2 = template2.invoke({'text': res_1.content})
res_2 = model.invoke(prompt_2)

print(res_2.content)