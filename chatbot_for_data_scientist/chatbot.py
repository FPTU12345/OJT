from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import json

memory = [SystemMessage(content = 'You are working with Data Sciencetist, and you only dealing with the csv file')]
class Data_Science_Chatbot:
  def __init__(self, functions):
    self.functions = functions
    self.llm = ChatOpenAI()
  
  def chat(self, input_text, memory):
    memory.append(HumanMessage(content = input_text))
    res = self.llm.predict_messages(memory, functions = self.functions)
    
    function = None
    if res.additional_kwargs != {}:
      function = (res.additional_kwargs['function_call']['name'],
                  json.loads(res.additional_kwargs['function_call']['arguments']))

    if function is None:
      memory.append(AIMessage(content = res.content))
      return memory, 'empty'
    else:
      if function[0] == 'EDA':
        memory.append(AIMessage(content = 'It is completed. Now you can see it at EDA'))
      elif function[0] == 'Processing':
        memory.append(AIMessage(content = 'It is completed. Now you can see it at Processing'))
      return memory, function
