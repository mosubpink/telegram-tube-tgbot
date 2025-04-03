import os
import logging

from environs import env
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

env.read_env()
token = env('token')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def yt_download(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    url = update.message.text
    try:
        with YoutubeDL() as dl:
            info_dict = dl.extract_info(url, download=True)
            video_file = dl.prepare_filename(info_dict)
            
            await update.message.reply_video(video_file)
            
            os.remove(video_file)
    except  Exception as Error:
            print(Error)

bot = ApplicationBuilder().token(token).build()

bot.add_handler(CommandHandler("start", hello))
bot.add_handler(MessageHandler(filters.Entity("url") ,yt_download))


bot.run_polling()

