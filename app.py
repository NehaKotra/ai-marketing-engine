import streamlit as st
from agent import run_marketing_agent
from pdf_reader import extract_pdf_text
from image_reader import extract_image_text
import re

st.set_page_config(
    page_title="Marketing Content Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
:root {
    --bg: #0a0a0f; --surface: #111118; --surface2: #18181f;
    --border: rgba(255,255,255,0.07); --accent: #7c5cfc; --accent2: #c084fc;
    --text: #f0eeff; --muted: #7a7a9a;
}
html, body, .stApp { background-color: var(--bg) !important; color: var(--text) !important; font-family: 'DM Sans', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem !important; max-width: 1200px !important; }
h1,h2,h3,h4 { font-family: 'Syne', sans-serif !important; }
.hero { text-align: center; padding: 3.5rem 1rem 2.5rem; }
.hero-tag { display: inline-block; background: rgba(124,92,252,0.15); border: 1px solid rgba(124,92,252,0.35); color: var(--accent2); font-size: 12px; font-weight: 500; letter-spacing: 2px; text-transform: uppercase; padding: 5px 16px; border-radius: 999px; margin-bottom: 1.2rem; }
.hero-title { font-size: clamp(2.2rem,5vw,3.8rem); font-weight: 800; line-height: 1.1; margin: 0 0 1rem; background: linear-gradient(135deg,#f0eeff 0%,#c084fc 60%,#7c5cfc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-sub { color: var(--muted); font-size: 1.05rem; font-weight: 300; max-width: 520px; margin: 0 auto; line-height: 1.7; }
.card-label { font-family: 'Syne',sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 0.75rem; }
.section-pill { display: inline-flex; align-items: center; gap: 6px; background: rgba(124,92,252,0.12); border: 1px solid rgba(124,92,252,0.25); color: var(--accent2); font-size: 11px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; padding: 4px 12px; border-radius: 999px; margin-bottom: 0.6rem; font-family: 'Syne',sans-serif; }
.output-block { background: var(--surface2); border: 1px solid var(--border); border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 1rem; }
.output-block:hover { border-color: rgba(124,92,252,0.3); transition: border-color 0.2s; }
.output-title { font-family: 'Syne',sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 0.75rem; }
.output-body { color: #c8c8e0; font-size: 0.92rem; line-height: 1.75; white-space: pre-wrap; }
.tag-website{color:#7c5cfc} .tag-social{color:#34d399} .tag-press{color:#60a5fa} .tag-news{color:#fbbf24} .tag-event{color:#f472b6} .tag-seo{color:#a78bfa} .tag-hashtag{color:#2dd4bf} .tag-strategy{color:#fb923c}
.divider { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
.stTextInput>div>div>input, .stTextArea>div>div>textarea { background: var(--surface2) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; color: var(--text) !important; font-family: 'DM Sans',sans-serif !important; font-size: 0.95rem !important; }
.stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus { border-color: rgba(124,92,252,0.6) !important; box-shadow: 0 0 0 3px rgba(124,92,252,0.1) !important; }
div[data-baseweb="select"]>div { background: var(--surface2) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; color: var(--text) !important; }
.stButton>button { background: linear-gradient(135deg,#7c5cfc,#c084fc) !important; color: white !important; font-family: 'Syne',sans-serif !important; font-weight: 700 !important; letter-spacing: 1px !important; font-size: 14px !important; border: none !important; border-radius: 10px !important; padding: 0.65rem 2.5rem !important; width: 100% !important; }
.stButton>button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }
.stFileUploader>div { background: var(--surface2) !important; border: 1px dashed rgba(124,92,252,0.35) !important; border-radius: 12px !important; }
.stSelectbox label,.stTextInput label,.stTextArea label { color: var(--muted) !important; font-size: 0.85rem !important; }
.stDownloadButton>button { background: transparent !important; color: var(--accent2) !important; border: 1px solid rgba(124,92,252,0.35) !important; border-radius: 10px !important; font-family: 'Syne',sans-serif !important; font-weight: 600 !important; font-size: 13px !important; width: 100% !important; }
.stDownloadButton>button:hover { background: rgba(124,92,252,0.1) !important; }
.stats-row { display: flex; gap: 12px; margin-bottom: 1.5rem; flex-wrap: wrap; }
.stat-chip { background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 8px 16px; font-size: 12px; color: var(--muted); }
.stat-chip span { font-weight: 600; color: var(--text); margin-right: 4px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-tag">⚡ AI-Powered</div>
    <h1 class="hero-title">Marketing Content Engine</h1>
    <p class="hero-sub">Turn any URL, document, or description into a full marketing campaign — instantly.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="card-label">01 — Choose your input</p>', unsafe_allow_html=True)
input_type = st.selectbox(
    "Input type",
    ["Website URL", "Text Description", "PDF Upload", "Image Upload"],
    label_visibility="collapsed",
)

st.markdown('<div style="margin-top:1.25rem"></div>', unsafe_allow_html=True)
st.markdown('<p class="card-label">02 — Provide your content</p>', unsafe_allow_html=True)

data = None

if input_type == "Website URL":
    data = st.text_input("URL", placeholder="https://yourwebsite.com", label_visibility="collapsed")

elif input_type == "Text Description":
    data = st.text_area("Description", placeholder="Describe your product, service, or company here...", height=140, label_visibility="collapsed")

elif input_type == "PDF Upload":
    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"], label_visibility="collapsed")
    if pdf_file:
        data = extract_pdf_text(pdf_file)
        st.success(f"PDF loaded — {len(data.split())} words extracted")

elif input_type == "Image Upload":
    img_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"], label_visibility="collapsed")
    if img_file:
        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(img_file, use_column_width=True)
        with col_info:
            with st.spinner("Analysing image..."):
                data = extract_image_text(img_file)
            st.success("Image analysed")
            st.caption(f"Caption: *{data}*")

st.markdown('<div style="margin-top:1.25rem"></div>', unsafe_allow_html=True)
st.markdown('<p class="card-label">03 — Generate</p>', unsafe_allow_html=True)
generate_btn = st.button("⚡  Generate Marketing Campaign")

SECTION_META = [
    ("website marketing content",  "Website Copy",       "tag-website",  "🌐"),
    ("social media posts",         "Social Media Posts", "tag-social",   "📱"),
    ("press release",              "Press Release",      "tag-press",    "📰"),
    ("newsletter content",         "Newsletter",         "tag-news",     "✉️"),
    ("event promotion",            "Event Promotion",    "tag-event",    "🎯"),
    ("seo keywords",               "SEO Keywords",       "tag-seo",      "🔍"),
    ("marketing hashtags",         "Hashtags",           "tag-hashtag",  "🏷️"),
    ("digital marketing campaign", "Campaign Strategy",  "tag-strategy", "🚀"),
]

def split_sections(raw: str):
    chunks = re.split(r'\n(?=\d+[\.\)])', raw)
    sections = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        lines = chunk.splitlines()
        heading = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        heading_lower = heading.lower()
        meta = None
        for keyword, label, css, icon in SECTION_META:
            if any(w in heading_lower for w in keyword.split()):
                meta = (label, css, icon)
                break
        if meta is None:
            meta = (heading, "tag-strategy", "📄")
        sections.append((meta[0], meta[1], meta[2], body or heading))
    return sections

if generate_btn:
    if not data:
        st.warning("Please provide some input first.")
    else:
        with st.spinner("Generating your campaign..."):
            result = run_marketing_agent(data)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown('<div class="section-pill">✦ Campaign Results</div>', unsafe_allow_html=True)

        sections = split_sections(result)
        word_count = len(result.split())
        char_count = len(result)
        sec_count  = len(sections)

        st.markdown(f"""
        <div class="stats-row">
            <div class="stat-chip"><span>{sec_count}</span> sections</div>
            <div class="stat-chip"><span>{word_count:,}</span> words</div>
            <div class="stat-chip"><span>{char_count:,}</span> characters</div>
        </div>
        """, unsafe_allow_html=True)

        if sections:
            pairs = [sections[i:i+2] for i in range(0, len(sections), 2)]
            for pair in pairs:
                cols = st.columns(len(pair))
                for col, (label, css, icon, body) in zip(cols, pair):
                    with col:
                        st.markdown(f"""
                        <div class="output-block">
                            <div class="output-title {css}">{icon} {label}</div>
                            <div class="output-body">{body}</div>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="output-block"><div class="output-body">{result}</div></div>', unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.download_button(
            "⬇  Download full campaign",
            result,
            file_name="marketing_campaign.txt",
            mime="text/plain",
        )