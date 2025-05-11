from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import At, Image, Plain
import os
import random

#插件名，作者，简介，版本号
@register("BasicFunc", "Fatima0323", "一个杂七杂八基础功能插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    #/helps 指令
    @filter.command("helps")
    async def helps(self, event: AstrMessageEvent):
        """查看可用指令列表""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    
        cmd_list = '''指令列表：
        /今日运势：查询今日运势，可使用“/转运”指令来转运
        /涩图：抽取一张随机涩图（虽然不一定真的涩）
        /kale：网卡的时候输入kale，BOT会温柔地安慰你'''

        message_chain = [
            At(qq=str(event.get_sender_id())),
            Plain(cmd_list)
        ]
        
        yield event.chain_result(message_chain)

    #/kale 指令
    @filter.command("kale")
    async def helloworld(self, event: AstrMessageEvent):
        """网卡的时候输入kale，BOT会温柔地安慰你""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        
        #图片选取
        pic_folder = os.path.join(os.path.dirname(__file__), "pic")
        image_files = [f for f in os.listdir(pic_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        image_file = random.choice(image_files)
        image_path = os.path.join(pic_folder, image_file)
        #message_chain结构
        message_chain = [
            At(qq=str(event.get_sender_id())),
            Plain(f"卡别叫!小笨蛋一个~"),
            Image.fromFileSystem(image_path)
        ]
        yield event.chain_result(message_chain)

    #/sese 指令
    @filter.command("sese", alias={'一份涩图','涩图','来一份涩图'})
    async def sesedetu(self, event: AstrMessageEvent):
        # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        """
        随机抽取一份涩图。欧耶~涩涩的图！（也可以输入“/涩图”，“/一份涩图”，“/来一份涩图”来获取随机涩图）
        """ 
        #随机图片
        setu_folder = os.path.join(os.path.dirname(__file__), "setu")
        image_files = [f for f in os.listdir(setu_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        image_file = random.choice(image_files)
        image_path = os.path.join(setu_folder, image_file)
        
        #随机回复
        reply_list = [
            "这是找小春同学要的图，才不是我收集的呢！哼~",
            "既然你那么想要，我就勉为其难地给你一张吧~",
            "让我给你变一张涩图出来，变~~~",
            "就知道涩图就知道涩图，少看一点嗷",
            "涩图，启动！"
        ]
        reply_content = random.choice(reply_list)
        
        message_chain1 = [
            At(qq=str(event.get_sender_id())),
            Plain(reply_content),
            Image.fromFileSystem(image_path)
        ]
        yield event.chain_result(message_chain1)

    #/今日运势 指令
    @filter.command("fortune", alias={'今日运势','转运'})
    async def fortune(self, event: AstrMessageEvent):
        # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        """
        查询今日运势，可使用“/转运”指令来转运
        """ 
        #随机图片
        folder = os.path.join(os.path.dirname(__file__), "luck_today")
        image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        image_file = random.choice(image_files)
        image_path = os.path.join(folder, image_file)

        message = event.message_str
        message_chain1 = [
            At(qq=str(event.get_sender_id())),
            Plain("当前运势："),
            Image.fromFileSystem(image_path)
        ]
        message_chain2 = [
            At(qq=str(event.get_sender_id())),
            Plain("今日运势："),
            Image.fromFileSystem(image_path)
        ]
        if "转运" in message:
            yield event.chain_result(message_chain1)
        else:
            yield event.chain_result(message_chain2)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
