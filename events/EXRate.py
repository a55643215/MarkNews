import requests 

def getCurrencyName(currency):
    currency_list = { 
        "USD" : "美元",
        "JPY": "日圓",
        "HKD" :"港幣",
        "GBP": "英鎊",
        "AUD": "澳幣",
        "CAD" : "加拿大幣",
        "CHF" : "瑞士法郎",  
        "SGD" : "新加坡幣",
        "ZAR" : "南非幣",
        "SEK" : "瑞典幣",
        "NZD" : "紐元", 
        "THB" : "泰幣", 
        "PHP" : "菲國比索", 
        "IDR" : "印尼幣", 
        "KRW" : "韓元",   
        "MYR" : "馬來幣", 
        "VND" : "越南盾", 
        "CNY" : "人民幣",
      }
    try: currency_name = currency_list[currency]
    except: return "無可支援的外幣"
    return currency_name


def getExchangeRate(msg):
    """

    sample
    code = '換匯USD/TWD/100;
    code = '換匯USD/JPY/100'
    """

    currency_list = msg[2:].split("/")
    currency = currency_list[0]
    currency1 = currency_list[1]
    money_value = currency_list[2]
    url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency   
    res = requests.get(url_coinbase)
    jData = res.json()
    pd_currency = jData['data']['rates']
    content = f'目前的兌換率為:{pd_currency[currency1]}{currency1}  \n查詢的金額為: '
    amount= float(pd_currency[currency1])
    content+=str('%.2f' % (amount * float(money_value))) + " " + currency1
    return content