
def sendMessage():
    import requests
    TOKEN = "6285365982:AAFkezDwVLHieSE16eQbiheohizJDYBV1fM"
    chat_id = "1290138656"
    message = "You are sleepy!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message