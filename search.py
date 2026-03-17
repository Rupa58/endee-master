# search.py
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load documents
if not os.path.exists("data/documents.txt"):
    os.makedirs("data", exist_ok=True)
    with open("data/documents.txt", "w") as f:
        f.write("Artificial Intelligence allows machines to simulate human intelligence.\n")
        f.write("Machine learning is a subset of AI.\n")
        f.write("Vector databases store embeddings for semantic search.\n")
        f.write("RAG combines search with language models for better answers.\n")

with open("data/documents.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = [model.encode(doc) for doc in documents]

# Semantic search function
def semantic_search(query, top_k=3):
    query_vec = model.encode(query)
    scores = [np.dot(query_vec, vec) for vec in embeddings]
    top_idx = np.argsort(scores)[::-1][:top_k]
    return [documents[i] for i in top_idx]