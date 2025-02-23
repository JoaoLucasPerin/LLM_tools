#-------------------------------------------------------
# Tools used: 
# Streamlit to web applications for machine learning,
# LangChain to applications for llm 
# Llama2 to the specific model for llm
#-------------------------------------------------------

#------------------------------------------------------
# Instructions:
# pip install streamlit langchain langchain-community langchain-core
# download the bin of the LLM in https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
# You can choose llama-2-7b-chat.ggmlv3.q2_K.bin, for example
# put the bin file in the same directory of this script
# type in Python Terminal:
# python -m streamlit run llm_poem_generator.py
# it will open your browser appropriately
#-------------------------------------------------------

import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title("AI Poem Generator")

content = st.text_input('Write a content of poem')

if st.button('Request a poem'):
    with st.spinner('writing a poem...'):
        result = llm.predict("write poem about "+content)
        st.write(result)

# Reference:
# https://www.youtube.com/watch?v=rdJVb8ZYR9c
########################################################################################################################
