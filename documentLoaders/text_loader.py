from langchain.document_loaders import TextLoader

loader = TextLoader("documentLoaders\aiml.txt", encoding ="utf-8") 
docs = loader.load() #load is a method of TextLoader class

print(docs)