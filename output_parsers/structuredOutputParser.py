from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

Llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "test-generation"
)

model = ChatHuggingFace(llm=Llm)

schema = [
    ResponseSchema(name='fact_1', description="fact 1 about the topic"),
    ResponseSchema(name='fact_2', description="fact 2 about the topic"),
    ResponseSchema(name='fact_3', description='fact 3 about the topic')
]
parser =StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

# prompt =template.invoke({'topic':'stephen hawking'})
# res = model.invoke(prompt)
res = chain.invoke({'topic':'stephen hawking'})
# final_res = parser.parse(res.content)
print(res)
# print(final_res)