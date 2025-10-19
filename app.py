from flask import Flask, request, jsonify
from newspaper import Article
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "News Summarizer API is live!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        url = data.get("url")
        if not url:
            return jsonify({"error": "Missing URL"}), 400

        print(f"📰 Received URL: {url}")
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            raise ValueError("Empty article text")

        summary = article.text[:700]
        print(f"✅ Newspaper3k parsed successfully! Title: {article.title}")

        return jsonify({"title": article.title, "summary": summary})

    except Exception as e:
        print(f"⚠️ Newspaper3k failed: {e}")
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            paragraphs = [p.get_text() for p in soup.find_all("p")]
            content = " ".join(paragraphs)
            return jsonify({
                "title": soup.title.string if soup.title else "Untitled",
                "summary": content[:700] if content else "No readable text found"
            })
        except Exception as inner_e:
            print(f"❌ Both methods failed: {inner_e}")
            return jsonify({"error": str(inner_e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
