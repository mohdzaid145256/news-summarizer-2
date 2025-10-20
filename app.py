@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        url = data.get('url', None)
        if not url:
            logging.error("Missing URL in request.")
            return jsonify({"error": "Missing URL"}), 400

        logging.info(f"Received URL: {url}")

        from newspaper import Article
        from bs4 import BeautifulSoup
        import requests
        from nltk.tokenize import sent_tokenize

        # Try Newspaper3k first
        try:
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
            logging.info("✅ Newspaper3k summarized successfully.")
            return jsonify(summary)
        except Exception as e:
            logging.warning(f"Newspaper3k failed, fallback activated: {e}")

        # === Fallback Summarizer ===
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, 'html.parser')
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        text = " ".join(paragraphs)

        if not text.strip():
            return jsonify({"error": "Unable to extract content."}), 400

        sentences = sent_tokenize(text)
        summary_text = " ".join(sentences[:5])  # take first 5 sentences

        return jsonify({
            "title": soup.title.string if soup.title else "Untitled Article",
            "summary": summary_text,
            "source_url": url
        })

    except Exception as e:
        logging.exception("Error while summarizing:")
        return jsonify({"error": str(e)}), 500
