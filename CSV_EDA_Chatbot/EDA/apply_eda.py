import json
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from EDA.word_frequency_analysis import WordFrequencyAnalysis
from EDA.word_length_analysis import WordLengthAnalysis

def response_encoder_for_processing(response):
  kwargs = response.additional_kwargs
  if kwargs:
    json_file = json.loads(kwargs['function_call']['arguments'])
  return json_file

def response_2_eda(response, df):
  kwargs = response_encoder_for_processing(response)

  # task
  task = kwargs['task']

  # x, y
  x = None
  y = None
  if 'column_name' in list(kwargs.keys()):
    x = kwargs['column_name']
  else:
    x, y = (kwargs['column_name1'], kwargs['column_name2'])

  # hue
  hue = None
  if 'categorized_column_name' in list(kwargs.keys()):
    hue = kwargs['categorized_column_name']
  
  if task == 'count':
    sns.countplot(x = x, hue = hue, data = df)
  elif task == 'scatter':
    sns.scatterplot(x = x, y = y, hue = hue, data = df)
  elif task == 'line':
    sns.lineplot(x = x, y = y, hue = hue, data = df)
  elif task == 'box':
    sns.boxplot(y = x, x = hue, hue = hue, data = df)
  elif task == 'wordcloud':
    wfa = WordFrequencyAnalysis(df, x).raw_display()
    wc = WordCloud().generate_from_frequencies(wfa)
    plt.imshow(wc)
    plt.axis('off')
  elif task == 'top_k_words':
    wfa = WordFrequencyAnalysis(df, x).top_k(k = kwargs['k'])
    sns.barplot(x = list(wfa.keys()), y = list(wfa.values()))
  elif task == 'word_length_analysis':
    wla = WordLengthAnalysis(df, x).number_display()
    sns.barplot(x = list(wla.keys()), y = list(wla.values()))
