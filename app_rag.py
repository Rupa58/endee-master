from endee import Endee, index
from sentence_transformers import SentenceTransformer
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

ENDEE_TOKEN = "YOUR_ENDEE_API_TOKEN"
ENDEE_URL = "https://api.endee.io"

# Initialize client and index
client = Endee(token=ENDEE_TOKEN, url=ENDEE_URL)
my_index = index.Index(token=ENDEE_TOKEN, url=ENDEE_URL, name="my_index")

# Add documents (only once)
my_index.upsert([
    {"id": "1", "text": "Machine Learning (ML) is a field of AI."},
    {"id": "2", "text": "Deep learning is a subfield of ML using neural networks."},
])

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def rag_search(query):
    query_vector = model.encode(query).tolist()
    results = my_index.search(query_vector, top_k=3)
    context = "\n".join([r['text'] for r in results])

    prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message["content"]

# Chat loop
print("AI RAG Search with Endee")
print("Type 'exit' to stop")

while True:
    question = input("Ask a question: ")
    if question.lower() == "exit":
        break
    answer = rag_search(question)
    print("Answer:", answer)