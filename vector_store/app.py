from Youtube_vector_store import Youtube_vector_store
import streamlit as st

st.title('Welcome to Youtube LangChain')
with st.sidebar:
  url_input = st.text_input('Enter the URL: ')
  question = st.text_input('Enter the question: ')
  button = st.button('Enter: ')

if url_input and question and button:
  test = Youtube_vector_store(url_input)
  res = test.ask(question)[0]
  st.write(res)
