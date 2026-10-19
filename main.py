import streamlit as st
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote

st.set_page_config(page_title="News Finder - Live", layout="wide")

st.markdown("""
<style>
.stApp { background: #f8fafc !important; }
.news-card { background:white; border-radius:16px; padding:16px; display:flex; gap:15px; border:1px solid #e2e8f0; margin-bottom:16px; box-shadow:0 4px 15px rgba(0,0,0,0.05); }
.news-card img { width:160px; height:110px; border-radius:12px; object-fit:cover; }
</style>
""", unsafe_allow_html=True)

st.title("📰 News Finder - LIVE")
st.write("Type anything - get real news!")

query = st.text_input("Search news", placeholder="Type: gate exams, sports, elections, AI, business... anything!")
search = st.button("✨ Search News", use_container_width=True)

def fetch_live_news(q):
    try:
        # Google News RSS - LIVE for any query
        encoded_q = quote(q)
        rss_url = f"https://news.google.com/rss/search?q={encoded_q}&hl=en-IN&gl=IN&ceid=IN:en"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(rss_url, headers=headers, timeout=10)
        
        root = ET.fromstring(resp.content)
        articles = []
        
        for item in root.findall(".//item")[:10]:
            title = item.find("title").text if item.find("title") is not None else "No Title"
            link = item.find("link").text if item.find("link") is not None else "#"
            desc = item.find("description").text if item.find("description") is not None else ""
            pub = item.find("pubDate").text if item.find("pubDate") is not None else ""
            
            # Clean description
            if "<" in desc:
                desc = desc.split("<")[0]
            
            # Random image based on query - so you always get picture
            img_url = f"https://picsum.photos/seed/{idx}{q}{title[:5]}/400/300"
            
            articles.append({
                "title": title,
                "description": desc[:200],
                "url": link,
                "pubDate": pub,
                "image": img_url
            })
        
        if articles:
            return articles
    except Exception as e:
        st.error(f"RSS Error: {e}")
    
    # If live fails, return at least something
    return []

if search or query:
    if not query:
        query = "india"
    
    with st.spinner(f"Fetching LIVE news for '{query}'..."):
        news_list = fetch_live_news(query)
    
    if news_list:
        st.success(f"✅ Found {len(news_list)} LIVE articles for '{query}'")
        for art in news_list:
            st.markdown(f"""
            <div class="news-card">
                <img src="{art['image']}" onerror="this.src='https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600'">
                <div>
                    <b style="font-size:15px;">{art['title']}</b><br>
                    <small style="color:#64748b;">{art['description']}...</small><br>
                    <small style="color:#94a3b8;">{art['pubDate']}</small><br>
                    <a href="{art['url']}" target="_blank" style="font-weight:bold; text-decoration:none;">Read More →</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No live news found, try different keyword like 'cricket' or 'GATE'")
else:
    st.info("👆 Type ANY topic above - like 'gate exams 2026', 'ipl', 'upsc', 'stock market' - and press Search")
