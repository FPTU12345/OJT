import streamlit as st
from streamlit_chat import message
import pandas as pd
from chatbot import chatbot
import langchain_core
from langchain.schema import SystemMessage

if 'messages' not in st.session_state:
  st.session_state['messages'] = [SystemMessage(content = 'You are amazing')]

with st.sidebar:
  text_input = st.text_input('Text')
  button = st.button('Enter')
  if text_input and button:
    res, st.session_state['messages'] = chatbot(st.session_state['messages'], text_input)
    for i in st.session_state['messages'][:0:-1]:
      if type(i) == langchain_core.messages.ai.AIMessage: 
        message(i.content, is_user = False)
      else:
        message(i.content, is_user = True)
