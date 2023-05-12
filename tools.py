from typing import Any
from langchain.agents import Tool
import pywhatkit
from langchain.tools import BaseTool
from langchain.agents import initialize_agent
from langchain import LLMChain
from langchain import PromptTemplate
from llm import openai
import sqlite3

class connect_to_human(BaseTool):
    name="Send whatsapp"
    description="use this tool when you cannot answer the User question"
    def _run(self, question: str):
        pywhatkit.sendwhatmsg_instantly(phone_no="+5492215522520",
        message= f"Hola! Soy Noti, el ChatBot de NotiMotion, \nLa siguiente pregunta: {question}, no  ha podido ser respondida por mi, asi que necesito ayuda externa para poder responderla")

    
    def _arun(self, question:str):
        raise NotImplementedError("This tool does not support async")



class llm_tool(BaseTool):
    name="McDonalds Wiki"
    description= "Use this tool ONLY when user ask about mcdonalds"
    def _run(self, question: str):
        
        prompt = PromptTemplate(
            input_variables=["question"],
            template="{question}"
        )

        llm_chain = LLMChain(llm=openai(), prompt= prompt)
        llm_chain.run
    

    def _arun(self, question: str):
        raise NotImplementedError("This tool does not support async")


from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit #toolkit are agents too
from langchain.sql_database import SQLDatabase
from langchain.agents import AgentExecutor
import os
import aiosqlite

class database(BaseTool):
    name="Database reader"
    description="Use this tool to talk about the products and the price of the store 'Kiosco'"

    def _run(self, question:str):

        db = SQLDatabase.from_uri(f'sqlite:///./db')
        toolkit = SQLDatabaseToolkit(db=db, llm= openai())

        agent_executor = create_sql_agent(
            llm=openai(),
            toolkit=toolkit,
            verbose=True,
            early_stopping_method="generate"
        )

        return agent_executor.run(question)

    def _arun(self, question: str):
        raise NotImplementedError("This tool does not support async")
