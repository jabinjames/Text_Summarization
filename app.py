import streamlit as st
from summarize import summarize

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Text Summarizer",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30 0%, #243B55 100%);
}

header {visibility: hidden;}

.glass-card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 0.4rem;
    margin: 2rem auto;
    max-width: 800px;
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.45);
}

.app-title {
    font-size: 2.6rem;
    font-weight: 700;
    color: #ffffff;
    text-align: center;
    
}

.app-subtitle {
    font-size: 1.1rem;
    color: #d1d5db;
    text-align: center;
    margin-bottom: 2.5rem;
}

.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 0.6rem;
}

.stTextArea textarea {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 14px;
    border: none;
    padding: 1.2rem;
    font-size: 1rem;
}

.stButton > button {
    background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
    color: white;
    border-radius: 14px;
    padding: 0.8rem;
    font-size: 1.05rem;
    font-weight: 600;
    width: 100%;
}

/* Summary container */
.summary-box {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 14px;
    padding: 1.4rem;
    height: 300px;              /* Always visible */
    overflow-y: auto;           /* Scroll if long */
    font-size: 1.05rem;
    line-height: 1.7;
    color: #111827;
}

.placeholder {
    color: #9ca3af;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
# Open the glass card
st.markdown('''
            <div class="glass-card">
            <div class="app-title">AI Text Summarizer</div>

            ''', unsafe_allow_html=True)





st.markdown(
    '<div class="app-subtitle">Fine-Tuned BART for Abstractive Summarization</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2, gap="large")

# -------- Input --------
with left:
    st.markdown('<div class="section-title">Input Text</div>', unsafe_allow_html=True)
    text = st.text_area(
        "Input",
        height=300,
        placeholder="Paste long text here ...",
        label_visibility="collapsed"
    )

    st.markdown('<div class="center-button">', unsafe_allow_html=True)
generate = st.button(" Generate Summary", use_container_width=False)
st.markdown('</div>', unsafe_allow_html=True)


# -------- Output (ALWAYS VISIBLE) --------
with right:
    st.markdown('<div class="section-title">Summary Output</div>', unsafe_allow_html=True)

    if generate and text.strip():
        with st.spinner("Summarizing..."):
            summary = summarize(text)

        st.markdown(
            f'<div class="summary-box">{summary}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="summary-box placeholder">Your summary will appear here...</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

