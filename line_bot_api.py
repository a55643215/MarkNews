from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# 必須放上自己的Channel Access Token
#ZENBtU+phh6cWcEWKnJiL1xkxIAZXuU+yOUjjKTdxKtjLmdnMUuE8UHmVmL9sgIIUaVxYvi9qbGWInPU6lYqh5m8zyGKwP4zRhpOKy+f8yIXHn9X08pJfvciarLZN46HyA44/zoyDxExJFlik+8nrAdB04t89/1O/w1cDnyilFU=
line_bot_api = LineBotApi('ZENBtU+phh6cWcEWKnJiL1xkxIAZXuU+yOUjjKTdxKtjLmdnMUuE8UHmVmL9sgIIUaVxYvi9qbGWInPU6lYqh5m8zyGKwP4zRhpOKy+f8yIXHn9X08pJfvciarLZN46HyA44/zoyDxExJFlik+8nrAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
#80a04bb05e0697a38fa7c0de2cf23052
handler = WebhookHandler('80a04bb05e0697a38fa7c0de2cf23052')