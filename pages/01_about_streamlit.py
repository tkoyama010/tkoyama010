from pathlib import Path

import streamlit as st

st.markdown(Path("pages/01_about_streamlit.md").read_text(), unsafe_allow_html=True)
