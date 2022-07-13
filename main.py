import os

import finnhub
from twilio.rest import Client

"""
quote function:
c: Current price
d: Change
dp: Percent change
h: High price of the day
l: Low price of the day
o: Open price of the day
pc: Previous close price
"""



def getGMEprice():
    finnhub_client = finnhub.Client(api_key=os.environ['FINNHUB_API_KEY'])
    quote = finnhub_client.quote('GME')
    return quote


def send_message(price):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] 
    client = Client(account_sid, auth_token)
    price = price
    distanceFrom = 1000 - float(price["c"])
    toSend = 'The price of GME went down by {}% and is now is: ${}. That is ${} away from $1000 >:)'.format(price["dp"], price["c"], distanceFrom)

    message = client.messages.create(  
                                messaging_service_sid='MG5eac5682678685d33bce1161ad5bc30f', 
                                body=toSend,
                                from_='+12513251057',      
                                to='+19166275849' 
                            )
    
    print(message.sid)

def checkStock():
    price = getGMEprice()
    if price["dp"] < 0:
        send_message(price)
    else:
        print("Price went up; no message sent.")

checkStock()