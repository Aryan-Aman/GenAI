from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

model= ChatOpenAI(model='gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY"))
st.header("Research Assistant")

# user_input=st.text_input("Enter the research paper you need to get summarry on !!")

select_paper=st.selectbox("Select a research paper", ["Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "DALL·E: Zero-Shot Text-to-Image Generation",
    "ResNet: Deep Residual Learning for Image Recognition",
    "Efficient:fake paper",
    "EfficientNet: Rethinking Model Scaling"])

input_style=st.selectbox(
    "Select the style of the summary",[
        "Mathematical","Code-oriented","Begineer-Friendly","Technical","Comprehensive"
    ]
)

input_length=st.selectbox(
    "Select the length of the summary",[
        "Short(1-2 paragraph)","Medium(3-5 paragraph)","Long(detailed explanation)"
    ]
)

template=load_prompt('template.json')

if st.button('summarize'):
    chain = template | model # template formed then passed to model
    response= chain.invoke(
    {
        "select_paper": select_paper,
        "input_style": input_style,
        "input_length": input_length
    }   
)
    st.write(response.content)  