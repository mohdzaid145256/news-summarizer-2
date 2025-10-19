from flask import Flask, request, jsonify
from newspaper import Article
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "News Summarizer API is live!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json(force=True)
        url = data.get("url")

        if not url:
            return jsonify({"error": "Missing 'url'"}), 400

        print(f"📰 Received URL: {url}")

        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            print("✅ Newspaper3k parsed successfully!")

            return jsonify({
                "title": article.title,
                "summary": article.summary
            })

        except Exception as e:
            print(f"⚠ Newspaper3k failed: {e}")
            # fallback to BeautifulSoup
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")

            paragraphs = [p.get_text() for p in soup.find_all("p")]
            content = " ".join(paragraphs)
            return jsonify({
                "title": soup.title.string if soup.title else "Untitled",
                "summary": content[:700] if content else "No summary available"
            })

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
