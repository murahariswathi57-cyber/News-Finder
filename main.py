import streamlit as st

st.set_page_config(page_title="News Finder", layout="centered")

# LIGHT THEME FIX
st.markdown("""
<style>
.stApp { background-color: #f8fafc !important; }
h1,h2,h3,p,label,span { color: #0f172a !important; }
div[data-testid="stTextInput"] input {
    background: white !important; border-radius: 25px !important;
    height: 55px !important; border: 1px solid #e2e8f0 !important;
}
div[data-testid="stSelectbox"] div { background: white !important; border-radius: 25px !important; }
.stButton button { background: #0f172a !important; color: white !important; border-radius: 25px !important; height: 55px !important; width: 100%; }
.news-card {
    background: white; border-radius: 16px; display: flex; gap: 15px;
    padding: 16px; margin-bottom: 16px; border: 1px solid #e2e8f0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.news-card img { width: 150px; height: 110px; border-radius: 12px; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>📰 News Finder</h1><p style='text-align:center;'>Explore latest stories</p>", unsafe_allow_html=True)

query = st.text_input("Search news", placeholder="e.g. gate exams")
category = st.selectbox("Choose a category", ["Education", "Technology", "Sports", "Business", "Health"])
search = st.button("✨ Search News")

# SAMPLE NEWS DATA WITH PICTURES - ALWAYS WORKS
sample_news = [
    {"title": "GATE 2026 Exam Dates Announced", "desc": "IIT announces GATE 2026 schedule, registration starts soon. Check eligibility and syllabus.", "img": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=500", "url": "https://gate2026.iisc.ac.in"},
    {"title": "Education Ministry Launches New Skill Program", "desc": "New initiative to boost employability for engineering graduates across India.", "img": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=500", "url": "https://www.education.gov.in"},
    {"title": "Top 5 Tips to Crack GATE Exams", "desc": "Experts share strategy, time management and best books for GATE preparation.", "img": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=500", "url": "#"},
]

if search:
    st.markdown(f"### 📚 Latest Discoveries for '{query}' - {category}")
    for news in sample_news:
        st.markdown(f"""
        <div class="news-card">
            <img src="{news['img']}">
            <div>
                <h4 style="margin:0 0 8px 0;">{news['title']}</h4>
                <p style="font-size:13px; color:#64748b !important; margin:0 0 10px 0;">{news['desc']}</p>
                <a href="{news['url']}" target="_blank" style="color:#0f172a; font-weight:bold; text-decoration:none;">Read More →</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Type something like 'gate exams' and click Search News")
