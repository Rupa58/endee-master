document.getElementById("askBtn").addEventListener("click", async () => {
    const query = document.getElementById("query").value;
    if (!query) return alert("Please type a question!");

    document.getElementById("answer").innerText = "Thinking...";

    const response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer;
});