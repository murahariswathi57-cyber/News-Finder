# --- PRO STYLE - ADD ONLY THIS ---
import streamlit as st
st.set_page_config(page_title="News Finder Pro", page_icon="📰", layout="centered")
st.markdown("""
<style>
    .stApp{background:#0e1117}
    .stTextInput input{background:#1e232f!important;border:1px solid #30363d!important;border-radius:12px!important;color:white!important;height:50px!important}
    .stButton button{background:linear-gradient(90deg,#238636,#1f6feb)!important;color:white!important;border-radius:12px!important;height:48px!important;font-weight:600!important;width:100%;border:none!important}
    .news-card{background:#161b22;border:1px solid #30363d;border-radius:14px;padding:18px;margin-top:12px}
</style>
""", unsafe_allow_html=True)
# --- YOUR OLD CODE CONTINUES BELOW ---
import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="News Finder", page_icon=" ")
st.title(" News Finder")
st.write("Search any topic - No API Key needed")

topic = st.text_input("Enter a topic", "technology")

if st.button("Search News"):
    with st.spinner("Finding news..."):
        url = f"https://news.google.com/rss/search?q={topic}&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url)
        root = ET.fromstring(response.content)
        news_list = root.findall("./channel/item")[:6]

        if not news_list:
            st.error("No news found. Try another topic.")
        else:
            for news in news_list:
                title = news.find("title").text
                link = news.find("link").text
                date = news.find("pubDate").text

                st.subheader(title)
                st.caption(date)
                st.link_button("Read Full News", link)
                st.divider()
