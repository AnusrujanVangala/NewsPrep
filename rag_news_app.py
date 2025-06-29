import streamlit as st
import feedparser
import requests
from bs4 import BeautifulSoup
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(model="llama3-8b-8192", groq_api_key="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")

# Prompt templates
note_prompt = PromptTemplate(
    input_variables=["context"],
    template="Summarise the following news article into concise bullet-point notes suitable for government exam preparation:\n{context}"
)
quiz_prompt = PromptTemplate(
    input_variables=["context"],
    template="Generate 3 multiple-choice questions with 4 options and the correct answer from this article:\n{context}"
)
importance_prompt = PromptTemplate(
    input_variables=["context"],
    template="Evaluate the following article and answer: Is it important for UPSC/SSC/RBI current affairs section? Provide a 1-line summary of why/why not:\n{context}"
)

# RSS feeds for stable access
rss_feeds = {
    "PIB": "https://pib.gov.in/rss.aspx",
    "The Hindu": "https://www.thehindu.com/news/national/feeder/default.rss",
    "Business Standard": "https://www.business-standard.com/rss",
    "Indian Express": "https://indianexpress.com/section/india/feed/",
    'Hindustan Times': "https://www.hindustantimes.com/rss/india/rssfeed.xml",
    "Times of India": "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms",
    "The Wire": "https://thewire.in/feed",
    "News18": "https://www.news18.com/rss/india.xml",
    "The Print": "https://theprint.in/feed/",
    "Scroll.in": "https://scroll.in/latest/rss",
    "The Quint": "https://www.thequint.com/feed",
    "Moneycontrol": "https://www.moneycontrol.com/rss/latestnews.xml",
    "Live Mint": "https://www.livemint.com/rss/homepage.xml",
    "Zee News": "https://zeenews.india.com/rss/india-national.xml",
    "NDTV": "https://feeds.feedburner.com/ndtvnews-india-news",
    "India Today": "https://www.indiatoday.in/rss/120latest-headlines/story.xml",
    "The Economic Times": "https://economictimes.indiatimes.com/rssfeedsdefault.cms",
    "The Telegraph": "https://www.telegraphindia.com/rss"
    }

st.title("📰 Government Exam RAG Assistant (RSS Mode)")
st.markdown("Generate notes, quizzes, and summaries from recent government news articles via RSS feeds.")

selected_source = st.selectbox("Choose a news source:", list(rss_feeds.keys()))
feed_url = rss_feeds[selected_source]

feed = feedparser.parse(feed_url)

article_titles = [entry.title for entry in feed.entries]
selected_article_title = st.selectbox("Select an article to analyse:", article_titles)
selected_entry = next((entry for entry in feed.entries if entry.title == selected_article_title), None)

if st.button("Process Selected Article"):
    try:
        article_url = selected_entry.link
        response = requests.get(article_url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        full_text = "\n".join(paragraphs)

        st.subheader("📌 Article Title:")
        st.write(selected_article_title)

        st.subheader("📰 Article Text:")
        st.write(full_text[:1000] + "...")

        context = full_text[:3000]

        # Notes Generation
        note_chain = LLMChain(llm=llm, prompt=note_prompt)
        notes = note_chain.run(context)
        st.subheader("📝 Generated Notes:")
        st.write(notes)

        # Quiz Generation
        quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt)
        quiz = quiz_chain.run(context)
        st.subheader("❓ Practice Quiz:")
        st.write(quiz)

        # Importance Rating
        importance_chain = LLMChain(llm=llm, prompt=importance_prompt)
        importance = importance_chain.run(context)
        st.subheader("⭐ Exam Relevance Summary:")
        st.write(importance)

    except Exception as e:
        st.error(f"Failed to process article: {e}")
