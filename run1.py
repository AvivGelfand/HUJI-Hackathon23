import os
import telebot

bot_token = os.environ.get("BOTTOKEN")
chat_id = os.environ.get("CHAT_ID")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


bot = telebot.TeleBot(bot_token)
import langchain

# from langchain import PromptTemplate, HuggingFaceHub, LLMChain

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# ##
llm_chain = LLMChain(
    prompt=prompt,
    llm=HuggingFaceHub(
        repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0, "max_length": 64}
    ),
)

# question = "What area is best for growing wine in France?"

# bot.send_message(chat_id, "Hackathon: began running")

# print(llm_chain.run(question))
# bot.send_message(chat_id, "hackathon began running!")
# bot_token = os.environ.get("BOTTOKEN")


import os

# load api token from environment variable HUGGINGFACE_TOKEN

# load api token from environment variable HUGGINGFACE_TOKEN
# load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("HUGGINGFACE_TOKEN")
# print(token)

# make sure langchain is installed

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm_chain = LLMChain(prompt=prompt,
#                      llm=HuggingFaceHub(repo_id="google/flan-t5-xl",
#                                         model_kwargs={"temperature":0,
#                                                       "max_length":64}))

llm_chain = LLMChain(
    prompt=prompt,
    llm=HuggingFaceHub(
        repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0, "max_length": 64}
    ),
)
