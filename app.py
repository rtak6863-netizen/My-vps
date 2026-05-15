from telegram.ext import Application, CommandHandler
import requests

TOKEN = "/8870873326:AAHw0osZfh1Y6HHxL2IBdfJrythNPKpWCDA"

async def start(update, context):
    await update.message.reply_text("ربات فارکس طلا فعال شد ✅")

async def gold(update, context):
    url = "https://api.gold-api.com/price/XAU"
    data = requests.get(url).json()

    price = data["price"]

    await update.message.reply_text(f"قیمت طلا: {price}$")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gold", gold))

app.run_polling()
