import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from openai import OpenAI
from _client import get_lifelogs
import json

def summarize_lifelogs(lifelogs, should_stream=True):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes transcripts."},
            {"role": "user", "content": f"Summarize the following transcripts: {lifelogs}"}
        ],
        stream=should_stream
    )
    if should_stream:
        for chunk in response:
            if chunk.choices[0].finish_reason is None:
                print(chunk.choices[0].delta.content, end='')
    else:
        return response.choices[0].message.content

def main():
    # Get transcripts, increasing limit to 100
    lifelogs = get_lifelogs(
        api_key=os.getenv("LIMITLESS_API_KEY"),
        limit=5
    )
    
    # Summarize transcripts
    summarize_lifelogs(lifelogs)

    # Save lifelogs to a text file
    with open("lifelogs.txt", "w") as file:
        for log in lifelogs:
            file.write(json.dumps(log) + "\n")  # Convert dict to JSON string

if __name__ == "__main__":
    main()
