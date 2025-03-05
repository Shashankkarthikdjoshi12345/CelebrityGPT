import os
from constants import OPENAI_KEY
from langchain_openai import ChatOpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = OPENAI_KEY

st.title('langchain demo with openai')
input_text = st.text_input('Search the topic you want')

llm = ChatOpenAI(temperature = 0.8)


if input_text : 
    response = llm.invoke(input_text)
    print("response", response)
    st.write(response.content)