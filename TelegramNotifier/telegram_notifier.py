import requests
token = "YOUR TOKEN"
chat_id = "YOUR CHAT ID"
message_text = "MESSAGE TO SEND"

url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message_text}"
requests.get(url_req)
requests.get(url_req)
requests.get(url_req)