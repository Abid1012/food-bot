‎import asyncio
‎from telegram import Bot
‎
‎TOKEN = "8729316019:AAGEvWCpxsSkT5Zc1Xw44z1ZCH-KWBcg2cE"
‎GROUP_ID = "-1003934516101"
‎
‎bot = Bot(token=TOKEN)
‎
‎async def main():
‎    await bot.send_message(
‎        chat_id=GROUP_ID,
‎        text="✅ BOT WORKING!"
‎    )
‎
‎asyncio.run(main())
