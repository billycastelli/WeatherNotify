# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACd1621b1159184a8fa76c82d767cb3882"
auth_token = "e7b71696eddd3d22a66d98c3e7b744fd"

client = Client(account_sid, auth_token)

def send(toNum: str, fromNum: str, message:str):
    toNum = "+" + toNum
    fromNum = "+" + fromNum
    client.api.account.messages.create(to = toNum,
                                       from_ = fromNum,
                                       body = message)



