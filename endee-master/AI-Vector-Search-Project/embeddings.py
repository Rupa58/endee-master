from sentence_transformers import SentenceTransformer
import json

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("data/documents.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Generate embeddings
embeddings = [model.encode(doc).tolist() for doc in documents]

# Save embeddings
with open("data/embeddings.json", "w") as f:
    json.dump({"documents": documents, "embeddings": embeddings}, f)

print("Embeddings generated and saved to data/embeddings.json")