import os

import streamlit as st


# =========================================================
# GROQ MODEL
# =========================================================

MODEL_NAME = "openai/gpt-oss-120b"


# =========================================================
# GET GROQ API KEY
# =========================================================

try:

    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

except Exception:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# =========================================================
# CHECK API KEY
# =========================================================

if not GROQ_API_KEY:

    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add it to Streamlit Secrets."
    )
