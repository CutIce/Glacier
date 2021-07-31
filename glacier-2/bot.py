from os import path
import nonebot
import bot_config

nonebot.init(bot_config)
nonebot.load_plugins(path.join(path.dirname(__file__), 'glacier-2'), 'glacier-2')

bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.run()