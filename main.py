# --- PRO STYLE - ADD ONLY THIS ---
import streamlit as st
st.set_page_config(page_title="News Finder Pro", page_icon="📰", layout="centered")
st.markdown("""
import streamlit as st
st.set_page_config(page_title="News Finder Pro", page_icon="📰", layout="wide")

st.markdown("""
<style>
    .stApp { background: #f8fafc !important; }
    .header {
        background: white;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid #e2e8f0;
    }
    .news-card {
        background: white;
        border-radius: 14px;
        padding: 0;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
        margin-bottom: 18px;
        display: flex;
    }
    .news-card img {
        width: 180px;
        height: 130px;
        object-fit: cover;
    }
    .stTextInput input {
        background: white !important;
        border-radius: 25px !important;
        height: 50px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER WITH PICTURE ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965879.png", width=80)
with col2:
    st.markdown("""
    <div class="header" style="text-align:left; margin:0; padding:10px 20px;">
        <h1 style="margin:0; color:#0f172a;">News Finder Pro</h1>
        <p style="margin:5px 0 0 0; color:#64748b;">Search any topic - No API Key needed • Live & Professional</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
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
