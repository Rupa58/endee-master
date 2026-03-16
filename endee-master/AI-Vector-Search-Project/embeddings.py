from endee import Endee, Precision
from sentence_transformers import SentenceTransformer

# Initialize client (no token required for dev; if you have one use Endee(token="YOUR_TOKEN"))
client = Endee()

# Create an index for your vectors (dimension = embedding size)
index_name = "semantic_search_index"
dimension = 384  # all-MiniLM-L6-v2 produces 384-dim vectors

# Create index if it doesn't already exist
try:
    client.create_index(
        name=index_name,
        dimension=dimension,
        space_type="cosine",
        precision=Precision.INT8D
    )
    print(f"📌 Index '{index_name}' created.")
except Exception as e:
    # Index might already exist
    print(f"⚠️ Could not create index (it may already exist): {e}")

# Get the index reference
index = client.get_index(name=index_name)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("data/documents.txt", "r") as f:
    documents = [doc.strip() for doc in f.readlines()]

# Upsert documents into the index
for i, doc in enumerate(documents):
    vector = model.encode(doc).tolist()
    index.upsert([
        {
            "id": f"doc_{i}",
            "vector": vector,
            "meta": {"text": doc}
        }
    ])

print("✅ Documents successfully added to Endee vector database!")