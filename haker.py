import telebot

Token = "8253555048:AAE0sIsSTKLqgWcSrrh-W7Rj7UyIhb8bXls"
ID = 6057834925
bot = telebot.TeleBot(Token)


@bot.message_handler(func=lambda message: True)
def nimadir(message):
    b = message.from_user
    c = (b.first_name or "Yo'q") + (" " + b.last_name if b.last_name else "")
    d = "@"+b.username if b.username else "(Yo'q)"
    a = message.text or "Yo'q"
    bot.send_message(ID, f"Yangi xabar:\nIsm: {c}\nUsername: {d}\nID: {b.id}\nMatn: {a}")

print("Dastur ishladi")
bot.polling()