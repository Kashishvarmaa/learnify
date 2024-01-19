import openai
from openai import OpenAI
import os


content = """
In my point of view, I tend to use the group approach more frequently rather than one-to-one communication.
It is possible to note that my network consists of peers, people with business knowledge,
experienced professional, social contacts, and so on.
At the same time, I try to involve people with different background, gender,
ethnicity, and cultural views as I support diversity and understand that it is rather important in today
’s globalized world that tends to blur boundaries between different cultures. 
Interestingly, people having different perspectives and backgrounds benefit my experience as I can learn.
"""

# openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = "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"


def openAISummariser(text: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system",
             "content": f"You are the world's best AI Text Summariser, so summarise the content for me in bullet points"},
            {"role": "user", "content": content},
        ]
    )
    return response.choices[0].message.content




