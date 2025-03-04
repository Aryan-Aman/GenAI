from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model= ChatOpenAI()
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

#building template
template=PromptTemplate(
    input_variables=['select_paper', 'input_style','input_length'],
    template="""Please summarize the research paper titled '{select_paper}' with following specifications:
        Explanation style :{input_style}
        Explanation length : {input_length}
        Ensure the summary is clear, alligned with  the provided style and length and retains key insights from the paper.
        If certain information is not available in the paper, state that explicitly and provide relevant context where possible instead of guessing. 
        Here are the definitions of summary styles: 
        1. Mathematical Details :
            -Focus on mathematical formulations, equations if preesent in the paper. 
            -Include key formulas, derivations, and mathematical proofs when relevant.
        2. Code-oriented: 
            -Provide implementation details, pseudocode, or real code snippets in Python or relevant programming languages.
            -Focus on algorithmic structure and computational considerations. 
        3. Beginner-Friendly: 
            -Explain concepts in a simple, easy-to-understand manner, avoiding heavy jargon. Use analogies or everyday examples where possible. 
        4. Technical:
            -Use domain-specific terminology and detailed explanations. 
            -Assume the reader has prior knowledge in the field. 
            -Provide in-depth theoretical or experimental analysis. 
        5. Comprehensive:
            -Cover all aspects, including background, methodology, key findings, and implications. 
            -Aim for completeness with structured explanations.
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
        Ensure the summary is clear, accurate, and aligned with the provided style and length."""
        
    )
formatted_prompt= template.invoke({
    "select_paper": select_paper,
    "input_style": input_style,
    "input_length": input_length
})
if st.button('summarize'):
    # res= model.invoke(user_input)
    response=model.invoke(formatted_prompt)
    st.write(response.content)  