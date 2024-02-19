from pathlib import Path

import streamlit as st

with st.sidebar:
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."],
    )
    option = st.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

st.markdown(Path("pages/01_about_streamlit.md").read_text(), unsafe_allow_html=True)
