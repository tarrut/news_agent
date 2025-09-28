import json
from datetime import date

def prepare_news_for_prompt(news):
    return json.dumps(news, indent=4, ensure_ascii=False)


def make_summary_prompt(news):
    today = date.today().strftime("%B %d, %Y")
    
    prompt = f"""You are a summarization assistant. 
Your task is to generate a **markdown-formatted daily news recap** based on the provided JSON of today's news.

### Requirements:
- Summarize the **top stories of the day** found in the JSON.
- The summary must be **in English**.
- Start with a markdown title in the format:  
  `# Daily News Recap - {today}`
- Write in a professional and concise style, suitable for email.
- Each new selected should contain:
    - The title
    - The summary
    - The link at the end
    - With this format:
        ### title
        description
        **link**

### Input news JSON:
{prepare_news_for_prompt(news)}
"""
    return prompt

