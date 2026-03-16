from endee import EndeeClient
from sentence_transformers import SentenceTransformer
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

client = EndeeClient()
model = SentenceTransformer("all-MiniLM-L6-v2")

def rag_search(query):
    query_vector = model.encode(query).tolist()
    results = client.search(query_vector, top_k=3)
    context = "\n".join([r['text'] for r in results])

    prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message['content']

print("AI RAG Search with Endee")
print("Type 'exit' to stop")

while True:
    question = input("Ask a question: ")
    if question.lower() == "exit":
        break
    answer = rag_search(question)
    print("Answer:", answer)