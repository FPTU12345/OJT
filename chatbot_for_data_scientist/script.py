from pydantic import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function

class EDA(BaseModel):
  '''If the data sciencetist demand you to draw a specific plot, then you don't have to draw it. 
     Instead, return to me JSON dictionary so that I knew what they want to draw.
     I hope that you understand little about Seaborn and Wordcloud libraries in Python'''
  task : str = Field(description = ''' For now, you will return either one of these task:
                                   +) 'bar' : Bar plot (1 column requirement)
                                   +) 'box' : Box plot (1 column requirement)
                                   +) 'line' : Line plot (2 columns requirement. 
                                                          This will be default when there is a data related to date time like yy/mm/dd or hh/mm/ss)
                                   +) 'hist' : Histogram (1 column requirement)
                                   +) 'scatter' : Scatter plot (2 columns requirement)
                                   +) 'wla' : Word length analysis (1 column requirement)
                                   +) 'wfa_wc' : Word frequency analysis with Word Cloud (1 column requirement)
                                   +) 'wfa_top_' + k : Word frequency analysis with top k. 
                                                    Top k refers to the the k highest frequqncies of word. 
                                                    When you return, return to the format like 'wfa_top_10' if is top 10,
                                                                                               'wfa_top_5' if is top 5
                                                    (1 column requirement)'''
                                   )
  
  first_column : str = Field(description = '''The required column. 
                                              Sometime people will call it x.''')
  second_column : str = Field(description = '''The optional column, because plot such as box plot and histograms only require 1 plot. 
                                               Sometime people will call it y. 
                                               If they said nothing, just considered it as None.''')
  hue : str = Field(description = '''The optional column. 
                                     This will be used if the data sciencetist want to visualize followed by a specific category.
                                     If they said nothing, just considered it as None''')

class Processing(BaseModel):
  '''To have a cleaner data, you will come here'''
  action : str = Field(description = '''It could be one of of these mentioned below:
                                        +) Handling missing value
                                        +) Drop columns
                                        +) Convert from data type to other data type''')

functions = [convert_pydantic_to_openai_function(EDA),
             convert_pydantic_to_openai_function(Processing)]
