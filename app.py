from flask import Flask, request, jsonify
from newspaper import Article
import logging

app = Flask(__name__)

# Enable debug logging for Render logs
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return jsonify({"message": "📰 News Summarizer API is live!"})

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        url = data.get('url', None)
        if not url:
            logging.error("Missing URL in request.")
            return jsonify({"error": "Missing URL"}), 400

        logging.info(f"Received URL: {url}")
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        summary = {
            "title": article.title,
            "authors": article.authors,
            "publish_date": str(article.publish_date),
            "summary": article.summary,
            "top_image": article.top_image
        }

        logging.info("✅ Article summarized successfully.")
        return jsonify(summary)

    except Exception as e:
        logging.exception("Error while summarizing:")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
