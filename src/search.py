from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()
SERPER_API_KEY=os.getenv('MY_KEY')
os.environ["SERPER_API_KEY"]=SERPER_API_KEY

def response(company):
    search = GoogleSerperAPIWrapper()
    query = f"site:linkedin.com/in/ 'Talent Acquisition' {company}"
    res = search.results(query)

    return res
