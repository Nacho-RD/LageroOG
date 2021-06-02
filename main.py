import discord
import os
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix='!')
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')

@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Anuncio", description=ctx.message.content[7:], color=0xFF5733)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=datetime.date(datetime.now()))
    await ctx.send(embed=embed)

client.run(os.environ['TOKEN'])