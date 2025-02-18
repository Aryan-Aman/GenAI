from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=28)

res=embedding.embed_query("deepseek is chinese opensource model")
print(str(res))