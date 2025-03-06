import os
from constants import OPENAI_KEY
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

# Load API Key from Streamlit Secrets
OPENAI_KEY = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(temperature=0.8, openai_api_key=OPENAI_KEY)


st.title('Celebrity GPT')
input_text = st.text_input('Enter celebrity name')


person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
event_memory = ConversationBufferMemory(input_key="dob", memory_key="description_history")

# First prompt: Get information about the celebrity
first_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}."
)

chain1 = LLMChain(llm=llm, prompt=first_prompt, verbose=True, output_key='person', memory=person_memory)

# Second prompt: Get birthdate of the person
second_prompt = PromptTemplate(
    input_variables=['person'],
    template="Provide only the birth date of {person} in 'Month Day, Year' format."
)

chain2 = LLMChain(llm=llm, prompt=second_prompt, verbose=True, output_key='dob', memory=dob_memory)

# Third prompt: Get major events on that date
third_prompt = PromptTemplate(
    input_variables=['dob'],
    template="List 5 major events that happened on {dob}. Explain each event in two lines."
)

chain3 = LLMChain(llm=llm, prompt=third_prompt, verbose=True, output_key='events', memory=event_memory)

# Combine chains in sequence
sequential_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'events'],
    verbose=True
)

def refresh():
    """Function to refresh the Streamlit app"""
    st.experimental_rerun()

if st.button("🔄 Refresh"):
    refresh()


if input_text:
    response = sequential_chain.invoke({'name': input_text})
    print("Response:", response)

    st.markdown(
        f"<h3><b><u>About {input_text}:</u></b></h3>",
        unsafe_allow_html=True
    )
    st.write(response['person'])

    st.markdown(
        f"<h3><b><u>Date of Birth:</u></b></h3>",
        unsafe_allow_html=True
    )
    st.write(response['dob'])

    st.markdown(
        f"<h3><b><u>Major Events:</u></b></h3>",
        unsafe_allow_html=True
    )
    st.write(response.get('events', 'No events found'))

    with st.expander('Person name'):
        st.info(person_memory.buffer)
    
    with st.expander('Events'):
        st.info(event_memory.buffer)
