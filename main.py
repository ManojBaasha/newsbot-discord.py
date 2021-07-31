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

def news(top_headlines):
    list_of_news_articles=top_headlines["articles"]
    for i in list_of_news_articles:
        source=i["source"]
        author=i["author"]
        title=i["title"]
        description=i["description"]
        url=i["url"]
        urltoimage=i["urlToImage"]
        publishedat=i["publishedAt"]
        content=i["content"]
        print(author,"\n\n\n", title,"\n\n\n", description,"\n\n\n", url,"\n\n\n", urltoimage,"\n\n\n", publishedat,"\n\n\n", content)

news(top_headlines)
