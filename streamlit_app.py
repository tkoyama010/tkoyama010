from pathlib import Path

import streamlit as st

st.markdown(Path("README.md").read_text(), unsafe_allow_html=True)
