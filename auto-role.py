import discord
import random

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_member_join(member):
    liste_bienvenue = [f'bienvenue à toi <@{member.id}>', f"bienvenue dans mon serveur <@{member.id}>", f"souhaitez la bienvenue à notre nouveau membre <@{member.id}>", f"<@{member.id}> fait son arrivée dans le serveur"]
    channel = client.get_channel("mettre l'id du salon dans lequel vous voulez que les messages soient envoyés ici")
    role = discord.utils.get(member.guild.roles, name='mettre le nom du rôle que vous voulez ajouter au nouveaux membres')
    await channel.send(liste_bienvenue[random.randint(0, 3)])
    await member.add_roles(role)

client.run("TOKEN")
