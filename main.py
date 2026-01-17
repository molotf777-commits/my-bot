import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user}')

@bot.command()
async def video(ctx, url):
    await ctx.message.delete()
    # تم تصحيح الرابط هنا ومسح النقطة الزيادة
    new_url = url.replace("instagram.com", "ddinstagram.com").replace("tiktok.com", "tnktok.com")
    await ctx.send(f"@everyone \n {new_url}")

keep_alive()
bot.run(os.environ.get('TOKEN'))