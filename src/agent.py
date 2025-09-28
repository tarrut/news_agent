from openai import OpenAI

from prompts.make_summary import make_summary_prompt

def get_mail_message(news):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5-nano",
        input=make_summary_prompt(news)
    )
    return response.output_text