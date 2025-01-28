from dotenv import load_dotenv 
import openai
from openai import OpenAI
import os
import datetime
import prompts
import time
import schedule

load_dotenv()
token = os.getenv("API_KEY")

client = OpenAI(
    api_key=token,
)

def fetch_completion(question, retries=3):
    for attempt in range(retries):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            )
            return completion.choices[0].message["content"]
        except Exception as e:
            print(f"aya it not working: {e}. Retrying in 10 seconds...")
            time.sleep(20)  # Wait before retrying
    return None

def run_it_six_am_sharp():
    for question in questions:
        answer = fetch_completion(question)
        if answer:
            print(answer)
        else:
            print("failed to chatgpt an answer")
        time.sleep(60)

""" schedule.every().day.at("6:00").do(run_it_six_am_sharp)

while True:
    schedule.run_pending()
    time.sleep(1) """

questions = prompts.give_them_to_me(datetime.datetime.now().strftime("%B %d, %Y"))
run_it_six_am_sharp()
