import telegram

token = '5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)