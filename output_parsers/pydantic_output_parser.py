from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

LLM = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "test-generation"
)

model = ChatHuggingFace(llm=LLM)

class Person(BaseModel):
    name : str = Field(description="name of person")
    age : int = Field(description="age of person")
    city : str = Field(description="name of city of person belongs to")

parser =PydanticOutputParser(pydantic_object=Person)

template =PromptTemplate(
    template="Generate the name, age and city of the fictional person from some famous {comic_book} \n {format_instruction}",
    input_variables={"comic book"},
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain = template | model | parser
final_res=chain.invoke({'comic_book':'batman'})

# prompt =template.invoke({'comic_book':'marvel'})
# print(prompt)
# res=model.invoke(prompt)
# final_res=parser.parse(res.content)
print(final_res)