# Day2
**AI ChatBot**

The AI development team at Xfusion is tasked with building a role-play chatbot using OpenAI's API.

Task Requirements:

Navigate to the /root/openaiproject/chatbot.py directory.

Create a client instance using api_key and base_url.

Use openai model=openai/gpt-4.1-mini

Define a variable prompt with the following content:

You are a friendly travel guide. Greet the user and ask where they want to go.

Send this prompt to the OpenAI chat model and store the result in variable nameresponse.

Extract and print the generated text reply from the response

Run the file after installing OpenAI in a virtual environment.


Notes:

Ensure you are working inside /root/openaiproject.

api_key&base_url are in /root/.bash_profile (typically OPENAI_API_KEY and OPENAI_API_BASE).

Install OpenAI inside a venv before running the script.

python3 -m venv venv && source venv/bin/activate && pip install openai

Use temperature=0.7&max_tokens=100.

Use hardcoded values for api_key&base_url when initializing the OpenAI client, or read them from environment variables via os.environ.get('OPENAI_API_KEY') and os.environ.get('OPENAI_API_BASE').

You are allowed a maximum of 10 requests. After this, you may encounter a rate limiter error. Therefore, use your requests judiciously.

**Ans**

Use the following implementation in `/root/openaiproject/chatbot.py`:

```python
import os
from openai import OpenAI

# Create OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

# Prompt variable
prompt = "You are a friendly travel guide. Greet the user and ask where they want to go."

# Send prompt to the chat model
response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=100
)

# Extract and print generated reply
print(response.choices[0].message.content)
```

Run the following commands:

```bash
cd /root/openaiproject

python3 -m venv venv
source venv/bin/activate
pip install openai

python chatbot.py
```

This meets all the requirements:

* Uses `OPENAI_API_KEY` and `OPENAI_API_BASE`.
* Creates an OpenAI client instance.
* Uses model `openai/gpt-4.1-mini`.
* Defines the required `prompt` variable.
* Stores the API result in a variable named `response`.
* Prints the generated text reply.
* Uses `temperature=0.7` and `max_tokens=100`.
