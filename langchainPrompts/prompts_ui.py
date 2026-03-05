from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
import streamlit as st
from temperature import get_model
from langchain_core.prompts import load_prompt



load_dotenv()

@st.cache_resource
def load_model():
    return get_model()

model = load_model()

st.header("Research tool")
    
# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "salman khan actor", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt("template.json")

prompts = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    "length_input":length_input,
})

if st.button("Summerize"):
    result = model.invoke(prompts)
    st.write(result.content)