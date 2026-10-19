import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="News Finder",
    page_icon="📰",
    layout="wide"
)

# Load the separate CSS file
css_file = Path(__file__).parent / "style.css"
if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# 3D-style hero section
st.markdown("""
<div class="hero">
    <div class="hero-art">
        <div class="news-object">📰</div>
        <div class="news-object">🔎</div>
        <div class="news-object">🌍</div>
    </div>
    <h1>News Finder</h1>
    <p>Explore the latest stories. Discover what matters.</p>
</div>
""", unsafe_allow_html=True)

# Search interface
st.markdown("### 🔎 Find your next story")

with st.container(border=True):
    query = st.text_input(
        "Search news",
        placeholder="Try technology, AI, sports or education..."
    )

    category = st.selectbox(
        "Choose a category",
        ["All News", "Technology", "Education",
         "Business", "Sports", "Science", "Health"]
    )

    search_clicked = st.button(
        "✨ Search News",
        use_container_width=True
    )

st.markdown("### 📰 Latest Discoveries")

if search_clicked:
    if query.strip():
        st.info(
            f"Search requested: {query.strip()} | "
            f"Category: {category}"
        )

        # CONNECT YOUR EXISTING NEWS SEARCH FUNCTION HERE.
        # Display the real news articles returned by that function.
    else:
        st.warning("Please enter a topic to search.")

else:
    st.markdown("""
    Explore topics such as **Artificial Intelligence**,
    **Technology**, **Education**, and **Science**.
    Enter a topic above to get started.
    """)
