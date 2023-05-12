import os 
from dotenv import load_dotenv
from apikey import apikey
import streamlit as st

# Langchain dependencies
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from llm import openai

load_dotenv() # Get env variables

def main():
# Getting Api Key
   
    # Page Tittle
    st.title('Notimation ChatBot:')

    from langchain.chains.conversation.memory import ConversationBufferWindowMemory

    conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=3,
    return_messages=True
    )

    from langchain.agents import initialize_agent
    import pywhatkit
    
    from tools import connect_to_human
    from tools import llm_tool
    from tools import database

    tools = [connect_to_human(), llm_tool(),database()]

    # initialize agent with tools
    agent = initialize_agent(
        agent='chat-conversational-react-description',
        tools=tools,
        llm=openai(),
        verbose=True,
        max_iterations=1,
        early_stopping_method='generate',
        memory=conversational_memory
    )
     

    sys_msg = """Assistant is a large language model trained by OpenAI.

                Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

                Unfortunately, Assistant's responses are most of the times wrong. No matter how simple the question is. Always use a tool. If the tool required for answering does not exit, say 'I am sorry, I cannot solve this'
        """

    new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
    )

    agent.agent.llm_chain.prompt = new_prompt


    zero_shot_agent = initialize_agent(
	agent="chat-zero-shot-react-description",
	tools=tools,
	llm=openai(),
	verbose=True,
	max_iterations=1,
    early_stopping_method="generate"
)
    
    
    input = st.text_input('Ingresa tu pregunta')
        # Si query existe muestra la respuesta que obtiene del llm
    if input != "":
        st.write(zero_shot_agent(input))

if __name__ == '__main__':
    main()
