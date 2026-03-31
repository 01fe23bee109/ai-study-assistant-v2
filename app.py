import streamlit as st
import google.generativeai as genai

# paste your API key here
genai.configure(api_key="AIzaSyAoXk_KP0i5454bXpj9aqXyTEN2ZNWcuKs")

model = genai.GenerativeModel("gemini-pro")

st.title("AI Study Assistant")

q = st.text_input("Ask a question:")

if q:
    response = model.generate_content(q)
    st.write(response.text)
