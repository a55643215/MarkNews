from line_bot_api import *


def stock_reply_other(stockNumber):
    content_text = "即時股價和K線圖"
    text_message = TextSendMessage(
                                text = content_text ,
                                quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="#+股票代號查詢", 
                                                    text="#"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="K線圖", 
                                                    text="@K"+stockNumber
                                                )
                                       ),
                                       ]
                            ))
    return text_message