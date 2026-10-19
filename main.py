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



         
