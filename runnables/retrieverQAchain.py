from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # NEW IMPORT
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Load and split document
loader = TextLoader(r"runnables\dox.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create embeddings and vectorstore
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)

# Set up retriever and LLM
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask a question using .invoke instead of .run
query = "What are key takeaways from document?"
ans = qa_chain.invoke(query)

print("Answer:", ans)
