import os
def sendMessage():
    import requests
    TOKEN = os.environ["TOKEN"]
    chat_id = os.environ["chat_id"] 
    message = "You are sleepy!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message
