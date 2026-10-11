
import telebot
import requests

bot = telebot.TeleBot("YOUR_BOT_TOKEN")


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Salam! Welcome to my shop")



@bot.message_handler(commands=["products"])
def products(message):
    response = requests.get("http://127.0.0.1:8000/products")

    data = response.json()

    if not data:
        bot.reply_to(message, "No products found")
    else:
        for product in data:
            text = (
                f"id : {product['id']} | "
                f"name : {product['name']} | "
                f"price : {product['price']} | "
                f"stock : {product['stock']}"
            )

            bot.send_message(message.chat.id, text)



bot.infinity_polling()
