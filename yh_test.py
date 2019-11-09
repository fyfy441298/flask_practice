#!/usr/bin/python2.6  
# -*- coding: utf-8 -*- 
# flask 核心处理模块
from flask import Flask
# app应用入口
app = Flask(__name__)


# 定义 路由和视图
@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
