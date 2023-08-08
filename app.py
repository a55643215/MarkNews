#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    message_text = str(event.message.text).lower()
    
    ######################## 使用說明 選單 油價查詢################################
    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)

    
    if event.message.text == "@想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    ################################ 股票區 ######################################
    if event.message.text == "@股價查詢":
        line_bot_api.push_message(uid,TextSendMessage("請輸入#加股票代號....."))

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """Hello! 您好，歡迎您成為 Master Finance 的好友！

我是Master 財經小幫手 

-這裡有股票，匯率資訊喔~
-直接點選下方【圖中】選單功能

-期待您的光臨！"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)        
    

if __name__ == "__main__":
    app.run()
