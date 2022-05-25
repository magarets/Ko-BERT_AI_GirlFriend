import telegram

token = ''
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)


