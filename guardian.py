import discord

# REEMPLAZÁ ESTOS DOS DATOS:
TOKEN = 'MTUwNTA2NDIzMjk5NDA4MjgzNg.Gdcdfo.S8QjD9yGCd062QPaN9L2yXEZcLJ0U9CXolFGWo'
ID_CANAL_DE_VOZ = 624831211550015508

class BotSostenedor(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def on_ready(self):
        print(f'Bot conectado como {self.user}. Buscando el canal...')
        canal = self.get_channel(ID_CANAL_DE_VOZ)
        
        if canal and isinstance(canal, discord.VoiceChannel):
            try:
                await canal.connect()
                print(f'¡Éxito! Conectado a: {canal.name}. Cuidando la racha.')
            except Exception as e:
                print(f'Error al conectar al canal de voz: {e}')
        else:
            print('No se encontró el canal de voz o el ID es incorrecto.')

client = BotSostenedor()
client.run(TOKEN)