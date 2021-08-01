import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord import Embed
from newsapi import NewsApiClient


##################################################################
client = discord.Client()
client= commands.Bot(command_prefix='n!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


with open('apikey.txt') as f:
    """ using a text file to store the discord bot token"""
    apikey = f.read()

with open('token.txt') as a:
    """ using a text file to store the discord bot token"""
    token = a.read()
######################################################################


@client.command()
async def news(ctx, *, Newstype=None):
    if Newstype == None:
        await ctx.send("Use n!<topic> to search for the type of news you want")
        
    
    top_headlines = newsapi.get_top_headlines(q=str(Newstype),
                                          language='en',)

    

    a = top_headlines["articles"]
#
    list_of_news_articles=top_headlines["articles"]
    c=0
    for i in list_of_news_articles:
        c=c+1
        source=i["source"]
        author=i["author"]
        title=i["title"]
        description=i["description"]
        url=i["url"]
        urlToImage=i["urlToImage"]
        publishedat=i["publishedAt"]
        content=i["content"]

        
        embed=discord.Embed(title=title, url=url, description=description, color=0x109319)
        embed.set_thumbnail(url=urlToImage)
        embed.set_footer(text="Click on the link for more info")
        await ctx.send(embed=embed)

        if c==5:
            break





    







########################################################################
newsapi = NewsApiClient(api_key=apikey)


#
#
#
#
#
#
#
#
#
#
#
#

#news(top_headlines)
client.run(token)