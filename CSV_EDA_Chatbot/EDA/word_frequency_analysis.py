from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

def WordCount(df, column):
  words = [point.split() for point in list(df[column])]
  all_words = [word for sublist in words for word in sublist]
  word_counts = Counter(all_words)
  return dict(word_counts)

class WordFrequencyAnalysis:
  def __init__(self, df, column):
    self.data = WordCount(df, column)
  
  def raw_display(self):
    return self.data
  
  def top_k(self, k = 10):
    res = {k: v for k, v in sorted(self.data.items(), 
                                   key=lambda item: item[1],
                                   reverse = True)[:k]}
    return res
