
import google.generativeai as genai
import os
from config import google_api_key

genai.configure(api_key = google_api_key)


generation_config = {
    "temperature" : 0.9,
    "top_p" : 1,
    "top_k" : 1,
    "max_output_tokens" : 2048,
}

safety_settings = []

model = genai.GenerativeModel(
    model_name = 'gemini-pro',
    generation_config = generation_config,
    safety_settings = safety_settings
)

def generate_response(prompt):

    prompt = "you're a discord bot named laymouna (lemon) that generate answers to questions and chats with people and i'm a guy on a discord server that wants to talk to you , you're a funny and sarcastic bot , just like your creator ali , i want to talk to you or a ask u this " + prompt + " , i want a super short message with your answer/response (one sentence)" 
    response = model.generate_content(prompt)

    print(response.text)
    return response.text

def answer(prompt):
    response = model.generate_content(prompt)

    print(response.text)
    return response.text

prompt = "hello how are you ?"

response = generate_response(prompt)

#print(response)

