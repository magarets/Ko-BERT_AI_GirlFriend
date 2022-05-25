## start chatting ##
# 디스코드 봇 토큰 : OTc4NjQ3NzkyODExNjQyOTcw.GIPLDG.9cCmzgQk2br6xDQbApB-1E0GNsg7t2gDXlUbaw
import discord
import PingPongWr
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

sessionID = 'frQrxsyFTIOYHtyebPxwTK+U7anJuLrZgw13PDWa9q2pw4FPKkRFaHubQaOVbJQLCpVK3Av4a0v9wyn/M5bz+g=='
url = "https://builder.pingpong.us/api/builder/627c7214e4b0d7787e92b6fe/integration/v0.2/custom/" + 'sessionid'  # 핑퐁빌더 Custom API URL
pingpong_token = "Basic a2V5OjQ0ZDdjN2ZmYTJkYTFmNTA2Zjg4ODhlMjEyYzk3MDg3"  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언
text = 'abcedfghijklmn'
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(message.content.split(' '))
    if not message.content.startswith(text):
        str_text = ' '.join((message.content.split(" ")))
        print(str_text)
        return_data = await Ping.Pong(session_id ="Example", text = str_text, topic = True, image = True, dialog = True) # 핑퐁빌더 API에 Post 요청
        await message.channel.send(f"{return_data['text']}")

print('start')
bot.run('OTc4NjQ3NzkyODExNjQyOTcw.GIPLDG.9cCmzgQk2br6xDQbApB-1E0GNsg7t2gDXlUbaw')