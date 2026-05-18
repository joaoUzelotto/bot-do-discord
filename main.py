import os
import discord
from discord.ext import commands
import asyncio
from services.ai_services import perguntar_ia

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Online como {bot.user}")

@bot.command()
async def ia(ctx, *, pergunta):
    # evita travar o bot enquanto a IA responde
    resposta = await asyncio.to_thread(perguntar_ia, pergunta)
    await ctx.send(resposta)

@bot.command()
async def fejaocomfarinha(ctx, *, pergunta):
    resposta = await asyncio.to_thread(perguntar_ia, pergunta)
    await ctx.send(f"esse é meu nome! Feijão com farinha! ☠️ {resposta}")

bot.run(os.getenv("DISCORD_TOKEN"))