from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

Llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "test-generation"
)

model = ChatHuggingFace(llm=Llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Generate the name, age, city, favourite dish of a fictional person from india \n {format_instruction}",
    input_variables= [],
    partial_variables={"format_instruction":JsonOutputParser().get_format_instructions()}
)
# prompt=template.format()#no  inp varb so not sending anything in format(), sending prompt as it is -static prompt
# res = model.invoke(prompt)
# final_res = parser.parse(res.content)
chain = template | model |parser
final_res = chain.invoke({}) # here always have to send argument if i/p var empty then empty dict
print(final_res)
print(type(final_res))