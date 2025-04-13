#import openaiembeddingd, faiss,openai
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai


#load doc
loader = TextLoader("docx.txt")
documents= loader.load()

#split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

#convert text into embeddings and store in faiss
vectorstore = FAISS.from_documents(documents)

#create a retriever(fetch relevant document)-semantic search
retriever = vectorstore.as_retriever()

#manually returieve relevant docs
query = "what are key takeaways from document?"
retrieved_dox = retriever.get_relevant_document(query)

#combine retrieved text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_dox])

#initialize llm
llm = openai(model_name="gpt-3.5-turbo", temperature=0.7)

#manually pass retrieved text to llm
prompt = f"Based on the following text, answer the questions : {query}\n\n{retrieved_text}"
ans = llm.predict(prompt)

#print answer
print("Answer : ", ans)