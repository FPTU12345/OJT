from collections import Counter
def WordLengthCount(df, column):
  words = [point.split() for point in list(df[column])]
  all_unique_words = list(set([word for sublist in words for word in sublist]))
  res = {word: len(word) for word in all_unique_words}
  return res

class WordLengthAnalysis:
  def __init__(self, df, column):
    self.data = WordLengthCount(df, column)
  
  def raw_display(self):
    return self.data
  
  def number_display(self):
    return dict(Counter([i for i in self.data.values()]))
