from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import csv

llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model_name='gpt-3.5-turbo')
master_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<Analysis>'
