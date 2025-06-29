# NewsPrep
Current Affairs Preperation

---

# 📰 Government Exam RAG Assistant (RSS Mode)

An AI-powered Streamlit app that helps government exam aspirants stay up-to-date with current affairs and economic news by automatically fetching articles from trusted Indian news sources via RSS feeds. The app generates concise notes, practice quizzes, and relevance ratings using a Retrieval-Augmented Generation (RAG) approach.

---

## ✨ Features

* 🔍 Select articles from top Indian news sources (PIB, The Hindu, HT, Indian Express, etc.)
* 📑 Generate UPSC/SSC-style bullet-point **notes** from news
* 🧠 Create multiple-choice **quizzes** from articles
* ⭐ Automatically assess **importance** for government exams
* 📰 Works with stable **RSS feeds** to avoid scraping issues

---

## 🛠 Tech Stack

| Component      | Tool/Library                 |
| -------------- | ---------------------------- |
| UI             | Streamlit                    |
| News Ingestion | RSS feeds via `feedparser`   |
| Web Parsing    | `requests` + `BeautifulSoup` |
| AI Model       | LangChain + Groq (`llama3`)  |

---

## 🚀 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/rag-news-app.git
cd rag-news-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your Groq API Key

Replace the placeholder in the script or use environment variables:

```bash
export GROQ_API_KEY=your_groq_api_key
```

### 4. Run the App

```bash
streamlit run rag_news_app.py
```

---

## 📡 Supported RSS Feeds

Includes feeds from:

* [PIB](https://pib.gov.in/rss.aspx)
* [The Hindu](https://www.thehindu.com/news/national/feeder/default.rss)
* [Hindustan Times](https://www.hindustantimes.com/rss/india/rssfeed.xml)
* [Live Mint](https://www.livemint.com/rss/homepage.xml)
* [Indian Express](https://indianexpress.com/section/india/feed/)
* [More…](https://github.com/yourusername/rag-news-app/blob/main/rss_sources.md)

---

## 📦 File Structure

```
├── rag_news_app_ui.py      # Streamlit app
├── requirements.txt
└── README.md
```

---

## 🧠 Use Cases

* Government exam prep (UPSC, SSC, RBI, State PSCs)
* Current affairs revision
* Quiz-based self-testing
* AI-powered note generation

---

## 🙌 Credits

* [LangChain](https://www.langchain.com/)
* [Groq LLMs](https://groq.com/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Streamlit](https://streamlit.io/)

---

## 📄 License

MIT License. Feel free to fork, modify, and use!

---
