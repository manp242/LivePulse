from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv('NEWS_API'))

sources = newsapi.get_top_headlines(q="meta", country="us", category="technology" )

print(sources)

