from typing import Union
from pydantic import BaseModel

class Boxplot(BaseModel):
  task: str = 'box'
  column_name: str
  categorized_column_name: Union[None, str]

class Countplot(BaseModel):
  task: str = 'count'
  column_name: str
  categorized_column_name: Union[None, str]

class Scatterplot(BaseModel):
  task: str = 'scatter'
  column_name1: str
  column_name2: str
  categorized_column_name: Union[None, str]

class Lineplot(BaseModel):
  task: str = 'line'
  column_name1: str
  column_name2: str
  categorized_column_name: Union[None, str]

class Wordcloud(BaseModel):
  task: str = 'wordcloud'
  column_name: str

class TopKMostFrequentWord(BaseModel):
  '''Top k of words that used the most in 1 column of csv file'''
  task: str = 'top_k_words'
  column_name: str
  k: int

class WordLengthAnalysis(BaseModel):
  task: str = 'word_length_analysis'
  column_name: str

class EDA(BaseModel):
  task: Union[Boxplot,
              Countplot,
              Scatterplot,
              Lineplot,
              Wordcloud,
              TopKMostFrequentWord,
              WordLengthAnalysis]
