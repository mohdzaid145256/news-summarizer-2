🧠 AI News Summarizer

A smart and modern web app that summarizes news articles using AI-powered natural language processing (NLP).
Built with Flask, Python, and Newspaper3k, and deployed seamlessly on Render with a fully responsive interface.

🚀 Live Demo
🔗 Web App: https://news-summarizer-2-q9t3.onrender.com
🔗 GitHub Repository: https://github.com/mohdzaid145256/news-summarizer-2

🧩 Overview
The AI News Summarizer simplifies how users consume information by extracting key insights from long news articles.
Simply paste a news article URL, and within seconds, you get a concise summary — clean, quick, and readable.
This project demonstrates:
Backend development with Flask
Text extraction using Newspaper3k
Integration of AI/NLP capabilities
Responsive UI and deployment on Render

⚙️ Tech Stack
Category	Technology
Backend	Flask (Python)
NLP Engine	Newspaper3k
Frontend	HTML, CSS, JavaScript
Deployment	Render
Version Control	Git & GitHub

🖼️ Screenshots
✅ API Successfully Running
(Backend confirmation on Render)
![API Live](./Screenshot%202025-10-20%20at%207.13.01 AM.png)

💻 Web Application Interface
(Beautifully designed, responsive frontend)
![App Interface](./Screenshot%202025-10-20%20at%207.33.39 AM.png)

🔹 System Flow

                ┌────────────────────────┐
                │      User Interface     │
                │  (HTML, CSS, JS, Flask) │
                └────────────┬────────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │        Flask API        │
                │  (Handles requests,     │
                │   manages routing, and  │
                │   invokes NLP module)   │
                └────────────┬────────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │  NLP Engine (Newspaper3k) │
                │ Extracts & summarizes     │
                │ news article content      │
                └────────────┬────────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │      Render Server      │
                │ Hosts the live backend  │
                │ & manages deployment     │
                └────────────────────────┘


🧠 How It Works
User enters a valid news article URL.
Backend extracts text using Newspaper3k.
AI summarizes the content.
The summarized text appears instantly in the UI.

📦 Setup Instructions
🪜 1. Clone the Repository
git clone https://github.com/mohdzaid145256/news-summarizer-2.git
cd news-summarizer-2
⚙️ 2. Install Dependencies
pip install -r requirements.txt
▶️ 3. Run Locally
python app.py
🌐 4. Open in Browser
http://127.0.0.1:5000/

🌍 Deployment
Deployed using Render’s auto-deploy system — pushing updates to main automatically triggers a rebuild and redeployment.
This ensures continuous delivery and a live, production-ready experience.

✨ Future Enhancements
Improve summarization accuracy with transformer-based models (e.g., BART, T5)
Add multilingual summarization
Implement dark/light mode toggle persistence
Integrate summary download (PDF or text format)

👨‍💻 Author
Mohd Zaid
📧 mohdzaid4919@gmail.com
🔗 GitHub Profile

⭐ If you liked this project, don’t forget to star the repo and share it!
💬 Feedback and contributions are always welcome!
