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
openAI_model = "gpt-3.5-turbo-1106"


def openAISummariser(text: str):
    response = openai.chat.completions.create(
        model=openAI_model,
        messages=[
            {"role": "system",
             "content": f"You are the world's best AI Text Summariser, so summarise the content for me in bullet points if no content is provided set a default value as 'Provide some content' "},

            {"role": "user", "content": text},
        ]
    )
    return response.choices[0].message.content


def openAIDoubtSolver(text: str):
    response = openai.chat.completions.create(
        model=openAI_model,
        messages=[
            {"role": "system",
             "content": f"You are the job is to solve the doubts of students effectievely by providing as much as possible correct info if no doubt is provided set default value as 'Please put your doubt here' "},
            {"role": "user", "content": text},
        ]
    )
    return response.choices[0].message.content


def openAINotesProvider(note_title, note_category, note_content, translation_language, note_level):
    response = openai.chat.completions.create(
        model=openAI_model,
        messages=[
            {"role": "system",
             "content": f"You have to create notes to the user based on following criterias and topics like Note title {note_title}, note category {note_category} note content "
                        f"{note_content} language {translation_language} notes level {note_level}. If any parameter is not provided auto detect parameters"},

            {"role": "user", "content": f"Generate me effective notes to study based on following parameters. Title{note_title} note category {note_category} note content "
                        f"{note_content} language {translation_language} notes level {note_level}"},
        ]
    )
    return response.choices[0].message.content
