# Listagens dos Import's
import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or

# Lista de Módulos
modulos = ["cogs.comando"]

# Evento da Bot-Bruna
client = AutoShardedBot(command_prefix="_", case_insensitive=True)

# Evento do on_ready
@client.event
async def on_ready():
    print(f"{client.user.name} Online.")
    await client.change_presence(activity=discord.Streaming(name="_comandos", url="https://www.twitch.tv/dilera"))


# Carregar modulos & token
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("NzY1NjI4NTk0NTkxNjI5MzIy.X4XlMQ.rsSqQktfyBv8dovqebZM_pzjyZU")


