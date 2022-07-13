from twilio.rest import Client
import finnhub
import os




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
    finnhub_client = finnhub.Client(api_key="cb6ptfiad3idq8jbm7cg")
    quote = finnhub_client.quote('GME')
    return quote


def send_message():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] 
    client = Client(account_sid, auth_token)
    price = getGMEprice()
    distanceFrom = 1000 - float(price["c"])
    toSend = 'The price of GME is: ${}. That is ${} away from $1000 >:)'.format(price["c"], distanceFrom)

    message = client.messages.create(  
                                messaging_service_sid='MGeac4403637e61cc02e94a915313c9024', 
                                body=toSend,      
                                to='+19166275849' 
                            )

send_message()