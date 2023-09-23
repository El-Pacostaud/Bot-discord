import discord
from discord.ext import commands
import wikipedia

client = commands.Bot(command_prefix='/', intents=discord.Intents().all())
wikipedia.set_lang('fr')

@client.event
async def on_ready():
     print("ready")
     print(str(client.all_commands))
     await client.change_presence(activity=discord.Streaming(name="Working here", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUMcmljayBhc3l0ZWxl"))


@client.command(name='wiki')
async def wiki(ctx, recherche: str):
    answer = wikipedia.page(recherche)
    await ctx.channel.send(f'# __{answer.title}__ \n ### {wikipedia.summary(recherche, sentences = 1)}')
    await ctx.channel.send(f'||{answer.url}||')


client.run("TOKEN")
