from flask import Flask, render_template, request
from search import semantic_search  # Your semantic search function

# Initialize Flask app
app = Flask(__name__)
@app.route('/')
def home():
    return "App is working 🚀"

# Homepage route — shows the form
@app.route('/')
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route('/ask', methods=['POST'])
def ask():
    # Get the query from the form (not JSON)
    query = request.form['query']
    
    # Call your semantic search function
    results = semantic_search(query)
    
    # Join results to display as HTML
    answer = "<br>".join(results)
    
    # Render the same template with answer
    return render_template("index.html", answer=answer, query=query)

# Run the app
import os

if __name__ == "__main__":
    print("Starting Flask app...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)