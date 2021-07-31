from nonebot.command import CommandSession
from nonebot.experimental.plugin import  on_command

__plugin_name__ = 'ping'
__plugin_usage__ = 'ping pong'

@on_command('ping', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('pong')