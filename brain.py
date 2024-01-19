import openai
from openai import OpenAI
import os
import apiKey

content = """
In my point of view, I tend to use the group approach more frequently rather than one-to-one communication.
It is possible to note that my network consists of peers, people with business knowledge,
experienced professional, social contacts, and so on.
At the same time, I try to involve people with different background, gender,
ethnicity, and cultural views as I support diversity and understand that it is rather important in today
’s globalized world that tends to blur boundaries between different cultures. 
Interestingly, people having different perspectives and backgrounds benefit my experience as I can learn.
"""
doubt = "Who is last person to land on moon and why has moon landing stopped recently"

openai.api_key = apiKey.API_KEY


def openAISummariser(text: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system",
             "content": f"You are the world's best AI Text Summariser, so summarise the content for me in bullet points"},
            {"role": "user", "content": text},
        ]
    )
    return response.choices[0].message.content


def openAIDoubtSolver(text: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system",
             "content": f"You are the job is to solve the doubts of students effectievely by providing as much as possible correct info"},
            {"role": "user", "content": text},
        ]
    )
    return response.choices[0].message.content






