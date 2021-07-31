from newsapi import NewsApiClient
import json

with open('apikey.txt') as f:
    """ using a text file to store the discord bot token"""
    apikey = f.read()


newsapi = NewsApiClient(api_key=apikey)

top_headlines = newsapi.get_top_headlines(q='sports',
                                          language='en',)


print(type(top_headlines))
print(top_headlines.keys())
a = top_headlines["articles"]
print(len(a))
for i in a:
    print(i.keys())
