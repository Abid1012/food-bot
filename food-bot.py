import asyncio
import schedule
import time
from telegram import Bot

TOKEN = "8729316019:AAGEvWCpxsSkT5Zc1Xw44z1ZCH-KWBcg2cE"
GROUP_ID = -1003934516101

bot = Bot(token=TOKEN)

async def send_food_question():
    await bot.send_message(
        chat_id=GROUP_ID,
        text="আগামীকাল বুয়া কি রান্না করবে? 🍛"
    )

def job():
    asyncio.run(send_food_question())

# TEST: sends every 1 minute
schedule.every().day.at("16:00").do(job)

print("Bot running...")

while True:
    schedule.run_pending()
    time.sleep(30)
