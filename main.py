import openai
import discord
from discord.ext import commands

openai.api_key = "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"

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name="preguntar")
async def preguntar(ctx, *, pregunta):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pregunta,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    respuesta = completion.choices[0].text.strip()
    await ctx.send(respuesta)








bot.run("MTEwMzM0MDMwNTg2MTg0MDkxNg.GgYEX9.gNvT9Fgs9nIA8g93a78ugEkvrMwS9WK_kbae3Q");

