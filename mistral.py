import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

qqq= os.getenv("key")

def query(prompt, max_retries=3):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": f"Bearer {qqq}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "stop": ["[INST]", "\nHost:", "[/INST]"]  # Prevent generating new instructions
        }
    }

    for _ in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            response_data = response.json()

            if isinstance(response_data, list):
                # Successful response
                return response_data
            elif "error" in response_data:
                # Model loading error - retry after delay
                print(f"Error: {response_data['error']} - Retrying...")
                time.sleep(5)
                continue

        except Exception as e:
            print(f"Request failed: {str(e)}")
            time.sleep(3)

    return [{"generated_text": "Sorry, I'm unable to respond right now. Please try again later."}]