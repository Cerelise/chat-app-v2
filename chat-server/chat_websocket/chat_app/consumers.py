import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.authtoken.models import Token
from chat_app.models import Userinfo


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.userinfo_id = self.scope["url_route"]["kwargs"]["userid"]
        # 获取房间路由
        # print(self.room_name)  # myroom
        print(self.scope["url_route"]["kwargs"]["userid"])

        # Join room group
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.channel_layer.group_add(self.userinfo_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print('断开连接')
        await self.channel_layer.group_discard(self.room_name,
                                               self.channel_name)

    async def receive(self, text_data):
        # 接收来自前端onMessage()发送的数据
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # 提取对象中的部分数据
        # msg_content = text_data_json["content"]
        # 获取用户的token
        token_str = text_data_json['content']['token']
        # print(token_str)

        # 读取token对应的数据库里的user 不允许直接读盘
        # user = Token.objects.get(key=token_str).user
        # userinfo = Userinfo.objects.get(belong=user)

        # 同步转异步 等待函数的返回
        userinfo = await getUserinfo(token_str)
        # print(userinfo)
        msg_content = getResponseData(userinfo, text_data_json)
        print(msg_content["code"])

        # 私聊发送通道
        if msg_content['code'] == 201:
            await self.channel_layer.group_send(str(msg_content["data"]["to"]),
                                                {
                                                    "type": "chat_message",
                                                    "message": msg_content
                                                })
            return

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name,
            {
                # 自定义事件
                "type": "chat_message",
                # 事件的具体内容
                "message": msg_content
            })

        # 将整理好的数据发送至前端
        # self.send(text_data=json.dumps({"message": msg_content}))

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


@sync_to_async
def getUserinfo(token):
    user = Token.objects.get(key=token).user
    userinfo = Userinfo.objects.get(belong=user)
    return userinfo


def getResponseData(userinfo, text_data):
    if text_data['code'] == 201:
        resp_data = {
            "code": text_data['code'],
            "id": userinfo.id,
            "nickName": userinfo.nickName,
            "avatar": str(userinfo.avatar),
            "data": text_data['content']['data'],
            # "to": text_data['content']['data']['to'],
            "from": userinfo.id
        }
        return resp_data
    resp_data = {
        "code": text_data['code'],
        "id": userinfo.id,
        "nickName": userinfo.nickName,
        "avatar": str(userinfo.avatar),
        "data": text_data['content']['data']
    }
    return resp_data