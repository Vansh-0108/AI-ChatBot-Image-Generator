from openai import OpenAI
from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

openai = OpenAI(
    api_key = "<secret-key>"
)

chat_log = []

@app.post('/')
async def chat (user_input: Annotated[str, Form()]):

    chat_log.append({'role': 'user', 'content': user_input})
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = chat_log,
        temperature = 0.6
    )

    bot_reponse = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_reponse})
    return bot_reponse