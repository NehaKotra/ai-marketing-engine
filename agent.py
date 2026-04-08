import os
from langchain_groq import ChatGroq
from prompts import marketing_prompt
from rag_engine import retrieve_brand_guidelines
from website_scraper import get_website_content
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

def run_marketing_agent(input_data):
    if isinstance(input_data, str) and input_data.startswith("http"):
        content = get_website_content(input_data)[:2000]
    else:
        content = str(input_data)[:2000]

    guidelines = retrieve_brand_guidelines()
    prompt = marketing_prompt(content, guidelines)
    response = llm.invoke(prompt)
    return response.content