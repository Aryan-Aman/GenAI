from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

model= ChatOpenAI(model='gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY"))
st.header("Research Assistant")

user_input=st.text_input("Enter the research paper you need to get summarry on !!")
if st.button('summarize'):
    res= model.invoke(user_input)
    st.write(res.content)
