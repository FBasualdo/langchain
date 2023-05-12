from langchain import OpenAI


OPENAI_API_KEY=  "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"

def openai():
    return OpenAI(openai_api_key=OPENAI_API_KEY, model_name='text-davinci-003', temperature=0.5)
