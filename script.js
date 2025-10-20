document.getElementById("summarizeBtn").addEventListener("click", async () => {
    const url = document.getElementById("urlInput").value.trim();
    const resultDiv = document.getElementById("result");
    const titleEl = document.getElementById("title");
    const summaryEl = document.getElementById("summary");
  
    if (!url) {
      alert("Please enter a valid news article URL.");
      return;
    }
  
    resultDiv.style.display = "block";
    titleEl.textContent = "⏳ Fetching summary...";
    summaryEl.textContent = "";
  
    try {
      const response = await fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
      });
  
      const data = await response.json();
  
      if (data.error) {
        titleEl.textContent = "⚠️ Error";
        summaryEl.textContent = "Something went wrong. Please check the URL.";
      } else {
        titleEl.textContent = data.title || "Summary";
        summaryEl.textContent = data.summary || "No summary available.";
      }
    } catch (err) {
      titleEl.textContent = "⚠️ Error";
      summaryEl.textContent = "Unable to connect to the API.";
    }
  });
  