import streamlit as st
import google.generativeai as genai

# safe API key usage
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

st.title("AI Study Assistant")

q = st.text_input("Ask a question:")

if q:
    response = model.generate_content(q)
    st.write(response.text)
