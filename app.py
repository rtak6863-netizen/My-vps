from telegram.ext import Application, CommandHandler
import requests

TOKEN = "8772201536:AAGsVb-yS7MPK2gpgN51gVgk_U7enkCodYw"

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
