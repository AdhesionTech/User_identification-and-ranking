# 加载凭证，获得token.pickle

import os
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from langchain.memory import ConversationBufferMemory
import json


# Gmail APIのスコープを設定
SCOPES = [
    # "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.readonly",
    # "https://www.googleapis.com/auth/gmail.labels",
    # "https://www.googleapis.com/auth/gmail.modify",
]

def get_credential():
    """
    アクセストークンの取得

    カレントディレクトリに pickle 形式でトークンを保存し、再利用できるようにする。（雑ですみません。。）
    """
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_id.json", SCOPES)
            # creds = flow.run_local_server()
            creds = flow.run_local_server(port=0)  # 启动本地服务器完成授权
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

        # memory = ConversationBufferMemory()
        # 保存 memory 内容到文件
        # with open("memory.json", "w") as file:
        #     json.dump([message.dict() for message in memory.chat_memory.messages], file)



    return creds

