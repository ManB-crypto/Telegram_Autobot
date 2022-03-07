import telepot

bot_token = 'BOT_TOKEN'
tel_id = ID_personal or group

bot = telepot.Bot(bot_token)
bot.sendPhoto(tel_id,photo=open(r'C:\\image.jpg', 'rb'),caption="evidence")
#bot.sendMessage(tel_id,'testing meesagsse')


