import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f0f7ff, #ffffff, #f5f0ff);
    color: #172554;
}

h1 {
    color: #4338ca;
    font-weight: 800;
}

.stTextInput input {
    background-color: white;
    color: #172554;
    border: 2px solid #c7d2fe;
    border-radius: 12px;
    padding: 12px;
}

.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #9333ea, #ec4899);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #3730a3, #7e22ce, #be185d);
    color: white;
    transform: scale(1.03);
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: white;
    border-radius: 14px;
}
</style>
st.markdown("""
/* Your existing CSS styling */

""", unsafe_allow_html=True)

# Add your 3D image code here
st.image("news_3d.png", use_container_width=True)

# Then your existing News Finder title and search code
st.title("📰 News Finder")
""", unsafe_allow_html=True)
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
