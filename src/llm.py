from openai import OpenAI
from src.config import OPENAI_KEY
from src.models import AiResponse
import time

client = OpenAI(api_key=OPENAI_KEY)


async def query_chatgpt(prompt):
    response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
            {
                "role": "system",
                "content": "You are an expert in writing professional and effective email replies."
            },
            {
                "role": "user",
                "content": prompt  
            }
        ],
            temperature=0.1,
            max_tokens=500,
            response_format=AiResponse,
        )
    return response.choices[0].message.parsed


async def process_text_with_llm(context, manifest):
    start_time = time.time()  # Record the start time

    prompt = f"""Please review the following email conversation:{context}
                Based on this conversation, generate **two** suggested email replies related to the following topic:{manifest}
                The replies should be professional, clear, and concise."""

    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            response = await query_chatgpt(prompt)
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            print(
                f"Total execution time: {elapsed_time:.2f} seconds for description --> {manifest}")  # Print execution
            # time
            # print(response)
            return response

        except Exception as ex:
            print(f"Exception occurred in chatgpt answer generation: {ex}")
            retries += 1
            time.sleep(2)  # Adjust sleep time as necessary

    elapsed_time = time.time() - start_time
    print(f"Total execution time (failed): {elapsed_time:.2f} seconds")
    raise Exception("Maximum retries reached. Unable to get a response from ChatGPT.")