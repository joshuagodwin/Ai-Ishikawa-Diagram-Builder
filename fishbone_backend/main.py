'''
Created by Joshua Godwin
Backend api for ai fishbone diagram creation tool
Ishikawa diagram, also known as a Fishbone or cause and effect diagram is a diagram that shows the causes of a certain event.
This tool allows users to create a fishbone diagram by inputting the main problem and getting Ai suggestions and help in determinging causes of the problem. Manual causes can be added and the diagram will update and generate new suggestions based on entries.
'''

from fastapi import FastAPI
from fishbone_backend.build_gemeni_request import build_messages
import os
import google.generativeai as genai
import uvicorn
from pydantic import BaseModel
from fishbone_backend.gemeni_function_caller import call_function
from fishbone_backend.gemeni_functions import gemeni_functions
GEMENI_API_KEY = os.getenv('GEMENI_API_KEY')

genai.configure(api_key=GEMENI_API_KEY)
app = FastAPI()

class Problem(BaseModel):
    problem: str

@app.post("/init_cause_categories")
async def init_cause_categories(problem: Problem):
    messages, tools = build_messages(problem=problem)

    print(f"tools: {tools}")
    print(f"messages: {messages}")
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        tools=tools
        )

    response = model.generate_content(messages)
    part = response.candidates[0].content.parts[0]
    #call function
    if part.function_call:
        causes_obj = call_function(part.function_call, gemeni_functions)
        causes_list = dict(causes_obj)
        print(causes_list)
        return causes_list
    else:
        return 'no function was called'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)