import json
from openai import OpenAI


def prepare_news_for_prompt(news):
    return json.dumps(news, indent=4, ensure_ascii=False)


def get_prompt(news):
    prompt = f"""You have the following task:

Next I will append a json with a recapitulation of today's news. I need you to return a summary writen in markdown that will be sended via mail.

Here are some instructions:
    - You must include the top stories of the day present in the json.
    - The mail has to be in english
    - The title has to be Daily News Recap - #todays date#

Here are the news:
{prepare_news_for_prompt(news)}
"""
    return prompt


def get_mail_message(news):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5-nano",
        input=get_prompt(news)
    )
    return response.output_text