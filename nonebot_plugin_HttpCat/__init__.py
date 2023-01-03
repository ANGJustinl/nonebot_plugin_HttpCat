from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,Message
from nonebot.params import CommandArg

from .httpcat import httpcat_msgs

http_cat = on_command('http_cat',aliases={'httpcat','http猫'}, priority=5, block=True)

@http_cat.handle()
async def _handle(code: Message = CommandArg()):
    url = "https://httpcats.com/{}.jpg".format(code)
    msgs = await httpcat_msgs('http://www.httpstatus.cn/{}'.format(code))  
    await http_cat.finish(msgs+MessageSegment.image(file=url, cache=False), at_sender=True)

#httpx异步 await httpcat_msg(code)
async def httpcat_msg(code):
    msgs = await httpcat_msgs('http://www.httpstatus.cn/{}'.format(code))
    return msgs

#url同步 httpcat_pic(code)
def httpcat_pic(code):
    url = "https://httpcats.com/{}.jpg".format(code)
    return str(url)