# Import necessary things

from pyrogram import Client, filters
from Bot_Details import *

# Create an instance for the client

app = Client("Pokemon Masters",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

# Start command Handler

@app.on_message(filters.command('start')&filters.private)
def start (bot,message):
    bot.send_message(message.chat.id,"Preparing to start Game ")





