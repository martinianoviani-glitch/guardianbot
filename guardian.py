import discord
import asyncio
from flask import Flask
from threading import Thread
import os

# 1. CONFIGURACIÓN DE LA WEB FALSA PARA ENGAÑAR A RENDER
app = Flask('')

@app.route('/')
def home():
    return "Bot activo y cuidando la racha 24/7"

def run_web_server():
    # Render nos da el puerto automáticamente en esta variable de entorno
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. CONFIGURACIÓN DEL BOT DE DISCORD
TOKEN = 'MTUwNTA2NDIzMjk5NDA4MjgzNg.GfVe4F.PDPxtAS1dNjUjgD90BHI9rFvQrggVHyuwoVP-c'
ID_CANAL_DE_VOZ = 624831211550015508


class BotSostenedor(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.voz = None

    async def on_ready(self):
        print(f'Bot conectado como {self.user}.')
        await self.conectar_al_canal()

    async def conectar_al_canal(self):
        canal = self.get_channel(ID_CANAL_DE_VOZ)
        if canal and isinstance(canal, discord.VoiceChannel):
            while True:
                if not self.voice_clients:
                    try:
                        self.voz = await canal.connect()
                        print(f'¡Conectado a: {canal.name}! Cuidando la racha.')
                    except Exception as e:
                        print(f'Error al conectar: {e}')
                await asyncio.sleep(10)
        else:
            print('ID de canal incorrecto.')

# 3. ARRANCAR AMBAS COSAS A LA VEZ
def mantener_vivo():
    t = Thread(target=run_web_server)
    t.start()

# Prende la web falsa en segundo plano
mantener_vivo()

# Prende el bot de Discord
client = BotSostenedor()
client.run(TOKEN)
