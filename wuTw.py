# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "xxxxxxx" #personal key removed from github for privacy
auth_token = "xxxxxx"

client = Client(account_sid, auth_token)

def send(toNum: str, fromNum: str, message:str):
    toNum = "+" + toNum
    fromNum = "+" + fromNum
    client.api.account.messages.create(to = toNum,
                                       from_ = fromNum,
                                       body = message)
