import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"data": "hello"}))

    async def disconnect(self, close_code):
        print("socket disconnected:+>:---------------------------------------", flush=True)
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def receive(self, text_data):
        print("hello=> ", text_data, flush=True)
        await self.send(text_data=json.dumps({"message": "received"}))

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event["data"]))
