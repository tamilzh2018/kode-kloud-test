**Day 1**
The datacenter AI Engineering team is developing tools to improve the clarity of developer-reported bugs. Developers often report issues informally, which makes them difficult to understand or reproduce.

You are tasked to build a Python-based AI Bug Description Clarifier that transforms such informal bug reports into clear, structured, and professional issue summaries.

Inside /root/openaiproject/bug_clarifier.py:

Initialize the OpenAI client using environment values (api_key and base_url).

Define a function clarify_bug(description: str) -> str that builds a parameterized prompt to rewrite the raw bug description.

Send this prompt to the OpenAI Chat Completion API.

Use the following configuration for the API call:

model: openai/gpt-4.1-mini
messages: user → the constructed prompt
max_tokens: 100
temperature: 0.0
Use the input bug report:

  App keeps crashing when I click save.

Store the AI response in a variable named response and print the clarified bug summary to the console.

Notes:

Function must use the developer's input description dynamically in the prompt.

Ensure you are working inside /root/openaiproject.

OpenAI credentials are available in /root/.bash_profile.

Use hardcoded values for api_key and base_url when initializing the OpenAI client or read them from environment variables via os.environ.get('OPENAI_API_KEY') and os.environ.get('OPENAI_API_BASE').

Before running bug_clarifier.py, set up a virtual environment:

python3 -m venv venv && source venv/bin/activate && pip install openai

Maximum of 10 API requests allowed before rate limiting.

**Ans:**
A complete solution that meets all the stated requirements is:

1. Change to the project directory:

```bash
cd /root/openaiproject
```

2. Create and activate the virtual environment, then install the OpenAI package:

```bash
python3 -m venv venv && source venv/bin/activate && pip install openai
```

3. Create `bug_clarifier.py` with the following contents:

```python
import os
from openai import OpenAI

# Initialize OpenAI client using environment values
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

def clarify_bug(description: str) -> str:
    prompt = f"""
Rewrite the following informal bug report into a clear, structured, and professional issue summary.

Bug Report:
{description}

Return a concise bug summary suitable for a bug tracking system.
"""

    completion = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=100,
        temperature=0.0
    )

    return completion.choices[0].message.content.strip()


# Input bug report
bug_report = "App keeps crashing when I click save."

# Store the AI response in a variable named response
response = clarify_bug(bug_report)

# Print the clarified bug summary
print(response)
```

4. Run the script:

```bash
python bug_clarifier.py
```

This implementation:

* Works inside `/root/openaiproject`.
* Uses `OPENAI_API_KEY` and `OPENAI_API_BASE` from the environment (credentials available through `/root/.bash_profile`).
* Uses the developer-provided bug description dynamically via the `description` parameter.
* Calls the Chat Completion API with:

  * `model="openai/gpt-4.1-mini"`
  * `max_tokens=100`
  * `temperature=0.0`
* Stores the generated output in a variable named `response`.
* Prints the clarified bug summary to the console.
* Makes only a single API request when executed.
