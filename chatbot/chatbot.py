from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def chatbot(memory, text):
  memory.append(HumanMessage(content = text))
  chat = ChatOpenAI()
  res = chat(memory).content
  memory.append(AIMessage(content = res))
  return res, memory
