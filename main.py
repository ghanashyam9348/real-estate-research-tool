# @Author: Dhaval Patel Copyrights Codebasics Inc. and LearnerX Pvt Ltd.

import streamlit as st
from rag import process_urls, generate_answer

# Page configuration
st.set_page_config(page_title="Real Estate Research", layout="wide")

st.title("🏠 Real Estate Research Tool")

# Sidebar for URL inputs
st.sidebar.header("📥 Input URLs")
url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

# Main content section
st.divider()
st.subheader("❓ Ask a Question")
query = st.text_input("Enter your question about the processed documents:")

placeholder = st.empty()

# Process URLs button
process_url_button = st.sidebar.button("🔄 Process URLs", use_container_width=True)
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!='']
    if len(urls) == 0:
        st.warning("⚠️ Please provide at least one valid URL")
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        with placeholder.container():
            with st.spinner("Processing URLs..."):
                for status in process_urls(urls, headers):
                    st.success(status)
        # Clear placeholder after processing
        placeholder.empty()

if query:
    try:
        with st.spinner("Generating answer..."):
            answer, sources = generate_answer(query)
        
        # Results section with better styling
        with st.container(border=True):
            st.markdown("### ✅ Answer")
            st.markdown(f"<p style='font-size: 16px; line-height: 1.6;'>{answer}</p>", unsafe_allow_html=True)
        
        # Sources section
        if sources:
            with st.container(border=True):
                st.markdown("### 📚 Sources")
                st.markdown("<p style='font-size: 14px; line-height: 1.8;'>", unsafe_allow_html=True)
                for source in sources.split("\n"):
                    if source.strip():
                        st.markdown(f"• {source}")
                st.markdown("</p>", unsafe_allow_html=True)
    except RuntimeError as e:
        st.error("❌ Please process URLs first before asking questions")
