# Streamlit libraries
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_chat import message
st.set_option('deprecation.showPyplotGlobalUse', False)

# Data analysis libraries
import pandas as pd

# Langchain libraries
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_core.messages.human import HumanMessage as human
from langchain_core.messages.ai import AIMessage as ai

# Data visualiztion
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Modules
from OJT.chatbot_for_data_scientist import chatbot
from OJT.chatbot_for_data_scientist import script
from OJT.chatbot_for_data_scientist.EDA import word_frequency_analysis
from OJT.chatbot_for_data_scientist.EDA import word_length_analysis

# st.session_state is a type of memory. The chatbot requires it to memorize the past.

if 'df' not in st.session_state:
  st.session_state['df'] = None

if 'messages' not in st.session_state:
  st.session_state['messages'] = [SystemMessage(content = 'You are working with Data Sciencetist, and you only dealing with the csv file. Some of the provided tool will help you for your task.')]

if 'output_for_eda' not in st.session_state:
  st.session_state['output_for_eda'] = None

if 'output_for_processing' not in st.session_state:
  st.session_state['output_for_processing'] = None

selected = option_menu('main menu', ['summary', 'EDA', 'Processing'], orientation = 'horizontal')


# I/ The side bar:
with st.sidebar:

# a/ Upload the file:
  file = st.file_uploader('Enter a csv file', type = 'csv')
  if file:
    st.session_state['df'] = pd.read_csv(file)

# b/ Chatbot:
  text_input = st.text_input('Enter a request with specific column name')
  button = st.button('Send')
  if text_input and button:
    Chatbot = chatbot.Data_Science_Chatbot(script.functions)
    st.session_state['messages'], f = Chatbot.chat(text_input, st.session_state['messages'])

    if f[0] == 'EDA':
      st.session_state['output_for_eda'] = f[1]
    elif f[1] == 'Processing':
      st.session_state['output_for_processing'] = f[1]

    i = 0
    for mess in st.session_state['messages'][:0:-1]:
      if type(mess) is ai:
        message(mess.content, is_user = False, key = 'ai_' + str(i))
      if type(mess) is human:
        message(mess.content, is_user = True, key = 'human_' + str(i))
      i += 1


# II/ The main page:
# a/ Summary: Show the data, data types and missing values for each column
if selected == 'summary' and file:
  st.dataframe(st.session_state['df'])
  st.write('Summarized information of the data')
  names = list(st.session_state['df'].columns)
  data_types = [st.session_state['df'][name].dtype for name in names]
  missing_values = [st.session_state['df'][name].isna().sum() for name in names]
  st.dataframe({'Name' : names,
                'Data type': data_types,
                'Missing values' : missing_values})

# b/ EDA: Show data analysis
if selected == 'EDA' and file:
  st.write(st.session_state['output_for_eda'])

  # Word Length Analysis
  if st.session_state['output_for_eda']['task'] == 'wla':
    wla = word_length_analysis.WordLengthAnalysis(st.session_state['df'], 
                                                  st.session_state['output_for_eda']['first_column'])
    res = wla.number_display()
    sns.barplot(x = res.keys(), y = res.values())
    st.pyplot()
    st.write(res)
  
  # Word Frequency Analysis with Word Cloud
  if st.session_state['output_for_eda']['task'] == 'wfa_wc':
    wfa = word_frequency_analysis.WordFrequencyAnalysis(st.session_state['df'],
                                                        st.session_state['output_for_eda']['first_column'])
    res = wfa.raw_display()
    wc = WordCloud().generate_from_frequencies(res)
    plt.imshow(wc)
    plt.axis('off')
    st.pyplot()
    st.write(res)

  # Word Frequency Analysis with top-k
  if st.session_state['output_for_eda']['task'][:8] == 'wfa_top_':
    wfa = word_frequency_analysis.WordFrequencyAnalysis(st.session_state['df'],
                                                        st.session_state['output_for_eda']['first_column'])
    res = wfa.top_k(k = int(st.session_state['output_for_eda']['task'][8:]))
    sns.barplot(x = res.keys(), y = res.values())
    st.pyplot()
    st.write(res)

# c/ Processing: Show the data that was processed
if selected == 'Processing':
  st.write(st.session_state['output_for_processing'])
