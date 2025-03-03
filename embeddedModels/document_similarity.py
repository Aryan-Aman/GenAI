from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=250)

documents=[
    "Mount Everest, the world's highest peak, towers at 8,848 meters above sea level in the Himalayas, challenging climbers with its extreme conditions.",
    "K2, also known as the Savage Mountain, is the second-highest peak on Earth, infamous for its treacherous ascent and harsh weather conditions.",
    "Mount Kilimanjaro, Africa’s tallest mountain, stands majestically with its snow-capped peak rising above the Tanzanian plains.",
    "The Matterhorn, one of the most recognizable peaks in the Alps, boasts a striking pyramid shape that has captivated mountaineers for centuries.",
    "Denali, formerly known as Mount McKinley, is North America's highest mountain, dominating the Alaskan wilderness with its icy slopes.",
    "Mount Fuji, Japan’s iconic stratovolcano, is renowned for its symmetrical beauty and cultural significance, drawing millions of visitors each year."
]

query = 'tell me about denali'

documents_embeddings= embedding.embed_documents(documents)
query_embeddings=embedding.embed_query(query)

'''6 vector sets and 1 red vector set > find similarity of red vec. with other 6 black vecs - send as a 2-D list in cosine similarity func
document_embeddings is already a 2D vector(6,N)'''
# print (cosine_similarity([query_embeddings], documents_embeddings)) #2D list [[0.4264024  0.36096222 0.20647496 0.29104083 0.3415831  0.23178748]]-represents similarity of query(red vec) with 1st, 2nd ...., sentences

scores=cosine_similarity([query_embeddings], documents_embeddings)[0] #[0] get 1D list directly access similarity scores as a simple list
index, score = (sorted(list(enumerate(scores)),key=lambda x : x[1])[-1])
print(query)
print(documents[index])
print(f"Similarity score is :{score}")