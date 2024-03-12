from EDA.script_for_eda import EDA
from Processing.script_for_processing import Processing
from EDA.apply_eda import response_2_eda
from Processing.apply_processing import response_2_df
from langchain.chat_models import ChatOpenAI
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

if 'memory' not in st.session_state:
  st.session_state['memory'] = [SystemMessage(content = 'You are an csv expert who works for data scienctist')]

def chatbot_for_csv_eda(input, memory):
  llm = ChatOpenAI()
  functions = [convert_pydantic_to_openai_function(EDA),
               convert_pydantic_to_openai_function(Processing)]
  memory.append(HumanMessage(content = input))
  res = llm.predict_messages(memory, functions = functions)
  memory.append(res)
  return res , memory

def post(res, df = None):
  if res.additional_kwargs:
    task = res.additional_kwargs['function_call']['name']
    if task == 'EDA':
      response_2_eda(res, df)
      st.pyplot()
    else:
      df = response_2_df(res, df)
      st.dataframe(df)
  else:
    st.write(res.content)

file_csv = st.file_uploader('CSV File', type = 'csv')
if file_csv:
  df = pd.read_csv(file_csv)
  text = st.text_input('Prompt a query: ')
  button = st.button('Submit')
  if button and text:
    res, st.session_state['memory'] = chatbot_for_csv_eda(text, st.session_state['memory'])
    post(res, df)
