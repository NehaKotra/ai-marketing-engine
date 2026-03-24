def marketing_prompt(content, guidelines):

    prompt = f"""
You are a professional digital marketing strategist.

Brand Guidelines:
{guidelines}

Business Information:
{content}

Generate the following:

1. Website marketing content
2. Social media posts
3. Press release
4. Newsletter content
5. Event promotion
6. SEO keywords
7. Marketing hashtags
8. Digital marketing campaign strategy

Make the response well structured.
"""

    return prompt