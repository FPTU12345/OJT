from langchain.chains import LLMChain
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

def EDA(text):
  task = ResponseSchema(name = 'task', description = '''There could be only one of 3: 
                                                        +) 'Word Length Analysis'
                                                        +) 'Word Frequency Analysis'
                                                        +) 'Others'
                                                      ''')
  column = ResponseSchema(name = 'column', description = '''A list of the name of columns. For example ['column_1', 'column_2', 'column_3'].
                                                            However, if the is only 1 column then the output will be 'column_1' ''')
  additional = ResponseSchema(name = 'additional', description = '''If he or she ask for Word Frequency Analysis, then the additional will be one of 3 based on what he or she demand the output:
                                                                 +) 'Data' : Data 
                                                                 +) 'Word Cloud' : Visualization
                                                                 +) 'Top' + k (with k is an integer) : Visualization

                                                                    If he or she ask for Word Length Analysis, then the additional will be one of 2 based on what he or she demand the output:
                                                                 +) 'Histogram' : Visualization
                                                                 +) 'Data' : Data 

                                                                    If nothing else, then it will be None
                                                                 ''')
  response_schemas = [task, column, additional]
  output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
  format_instructions = output_parser.get_format_instructions()
  llm = ChatOpenAI()
  prompt = ChatPromptTemplate(messages = [HumanMessagePromptTemplate.from_template('''
                                                                                   You are working with csv file:
                                                                                   Input : {text}
                                                                                   Output : {format_instructions}
                                                                                   ''')],
                              input_variables = ['text'],
                              output_parser = output_parser,
                              partial_variables = {'format_instructions' : format_instructions})
  chain = LLMChain(prompt = prompt, llm = llm)
  res = chain.predict_and_parse(text = text)
  return res
