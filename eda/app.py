# Web
import streamlit as st
# Data analysis
import pandas as pd
# Data visualization
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Manual modules
from llm_csv import EDA
from word_frequency_analysis import WordFrequencyAnalysis
from word_length_analysis import WordLengthAnalysis

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('EDA-with-CSV')
df = pd.read_csv('cleaned_search_term.csv')
df.dropna(inplace = True)
input_text = st.text_input('Fill the request with the specific column name')
button = st.button('Submit')

if button and input_text:
  res = EDA(input_text)
  if res['task'] == 'Word Length Analysis':
    wla = WordLengthAnalysis(df = df, column = res['column'])

    if res['additional'] == 'Histogram':
      data = wla.number_display()
      fig = plt.subplot()
      fig.bar(x = list(data.keys()), height = list(data.values()))
      plt.xticks(rotation = 90)
      st.pyplot()
    
    if res['additional'] == 'Data':
      st.write(wla.raw_display())
      st.write(wla.number_display())

  if res['task'] == 'Word Frequency Analysis':
    wfa = WordFrequencyAnalysis(df = df, column = res['column'])

    if res['additional'] == 'Word Cloud':
      wordcloud = WordCloud().generate_from_frequencies(wfa.raw_display())
      plt.imshow(wordcloud)
      plt.axis('off')
      st.pyplot()
    
    if res['additional'][:4] == 'Top ':
      data = wfa.top_k(k = int(res['additional'][4:]))
      fig = plt.subplot()
      fig.bar(x = list(data.keys()), height = list(data.values()))
      plt.xticks(rotation = 90)
      st.pyplot()      
    
    if res['additional'] == 'Data':
      st.write(wfa.raw_display())
      

