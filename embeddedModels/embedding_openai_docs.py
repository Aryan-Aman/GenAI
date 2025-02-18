from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=28)

documents=[
    "This is a sample document.",
    "deepseek is chinese opensource model"
    "delhi is capital of india"
]

res=embedding.embed_documents(documents)
print(str(res))