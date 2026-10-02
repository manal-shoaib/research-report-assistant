import os
import streamlit as st


MODEL_NAME = "openai/gpt-oss-120b"

# Get the key from Streamlit Secrets
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing from Streamlit Secrets."
    )

# Make it available to CrewAI / LiteLLM / Groq
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
