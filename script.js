const summarizeBtn = document.getElementById("summarizeBtn");
const urlInput = document.getElementById("urlInput");
const loader = document.getElementById("loader");
const output = document.getElementById("output");
const toggle = document.getElementById("toggle");
const API_URL = "https://news-summarizer-2-q9t3.onrender.com/summarize"; // Flask backend
// Typing animation function
function typeText(element, text, speed = 25) {
  element.innerHTML = "";
  let i = 0;
  function typing() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(typing, speed);
    }
  }
  typing();
}
summarizeBtn.addEventListener("click", async () => {
  const url = urlInput.value.trim();
  if (!url) {
    output.classList.remove("hidden");
    output.style.color = "red";
    output.textContent = "⚠️ Please enter a valid article URL.";
    return;
  }
  loader.classList.remove("hidden");
  output.classList.add("hidden");
  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });
    const data = await res.json();
    loader.classList.add("hidden");
    output.classList.remove("hidden");

    if (data.error) {
      output.style.color = "red";
      output.textContent = `❌ Error: ${data.error}`;
    } else {
      output.style.color = "inherit";
      const summaryText = `📰 <b>${data.title}</b>\n\n${data.summary}`;
      typeText(output, summaryText, 20);
    }
  } catch (err) {
    loader.classList.add("hidden");
    output.classList.remove("hidden");
    output.style.color = "red";
    output.textContent = "❌ Request failed. Please try again.";
  }
});
// Theme toggle
toggle.addEventListener("change", () => {
  document.body.classList.toggle("light");
});
