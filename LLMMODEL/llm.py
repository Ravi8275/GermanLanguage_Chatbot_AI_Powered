import openai
from dotenv import load_dotenv
import os

load_dotenv()

Openai_api_key=os.getenv("OPENAI_API_KEY") #Getting the OPENAI api key


def generate_response(prompt):
    response=openai.Completion.create(
    model="gpt-3.5-turbo", #Model 
    messages=[
        {"role":"system","content":"you are my assistan"}, 
        {"role":"user","content":prompt}
    ], #Assigning roles
    max_tokens=150, #setting the output range
    temperature=0.7, #Setting the randomness of the model output
    )
    return response.choices[0].message['context'].strip() #retrieving the very first/best response of the model to the prompt


prompt = "What is the capital of France?"
response = generate_response(prompt)
print(response)