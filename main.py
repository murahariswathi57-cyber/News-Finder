import streamlit as st

st.set_page_config(
    page_title="News Finder",
    page_icon="📰",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#dbeafe,#f3e8ff,#fce7f3);
}
.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#4f46e5;
}
.subtitle {
    text-align:center;
    color:#475569;
    font-size:18px;
}
.news {
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0 10px 25px #6366f144;
    margin:15px 0;
    border-left:5px solid #8b5cf6;
}
.news:hover {
    transform:translateY(-5px);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📰 News Finder</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Discover stories. Explore the world.</div>',
    unsafe_allow_html=True
)

st.write("")

topic = st.text_input(
    "🔎 Search News",
    placeholder="Enter a topic, e.g. AI, technology, sports..."
)

if st.button("✨ Find News", use_container_width=True):
    if topic.strip():
        st.subheader(f"📰 Explore: {topic}")
        st.info(
            "This demo does not fetch live news. "
            "Connect a news API to display real articles."
        )

st.markdown("""
<div class="news">
<h3>🌍 World News</h3>
<p>Explore international events and important global developments.</p>
</div>
<div class="news">
<h3>💻 Technology</h3>
<p>Discover innovations in AI, software, and digital technology.</p>
</div>
<div class="news">
<h3>🚀 Science & Innovation</h3>
<p>Explore discoveries shaping our future.</p>
</div>
""", unsafe_allow_html=True)

st.caption("News Finder | Explore knowledge, one story at a time.")
