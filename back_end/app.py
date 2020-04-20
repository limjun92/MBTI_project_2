from flask import Flask, request
from flask_cors import CORS
import os
import sys
import urllib.request
import json
client_id = "DDViAHj1CzTI3Xhuvbxg"
client_secret = "l9wT2TKdy0"
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/parse')
def hello_world():
    return 'Hello World'
@app.route('/click')
def click():
    return 'result'
@app.route('/post',methods=['POST'])
def post():
    print("asdasdasda")
    post_data = request.data
    print("ㅁㄴㅇ",post_data)
    return post_data

@app.route('/trans',methods=['POST'])
def trans():
    print("번역하러왔어요")
    post_data = request.data
    encText = urllib.parse.quote(post_data)
    print(encText)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)
    res = urllib.request.urlopen(req, data=data.encode("utf-8"))
    print(type(res))
    rescode = res.getcode()
    print(type(rescode))
    if(rescode==200):
        response_body = res.read()
        print(type(response_body))
        str = response_body.decode('utf-8')
        dict = json.loads(str)
        return dict['message']['result']['translatedText']
    else:
        return "Error Code:" + rescode
     
if __name__ == '__main__':
  app.run(host='0.0.0.0')