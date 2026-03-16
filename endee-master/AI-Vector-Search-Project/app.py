from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Artificial Intelligence allows machines to simulate human intelligence.",
    "Machine learning is a subset of AI.",
    "Vector databases store embeddings for similarity search.",
    "Retrieval Augmented Generation combines search with language models."
]

doc_vectors = model.encode(documents)

def semantic_search(query):
    query_vector = model.encode(query)
    scores = np.dot(doc_vectors, query_vector)
    best_match = np.argmax(scores)
    return documents[best_match]

print("AI Semantic Search")
print("Type 'exit' to stop")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    answer = semantic_search(question)
    print("Answer:", answer)