from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv('NEWS_API'))

top_headlines = newsapi.get_top_headlines(q='ICE',
                                          sources='bbc-news,the-verge',
                                          category='general',
                                          language='en',
                                          country='us')


print(top_headlines)