# AssistX

## 简介 
一个桌面人工智能助手。

## 实现原理
提出问题后，请求服务器（基于ChatGLM3）获得回复和历史记录，同时，我们将会支持许多额外功能（目前：OCR、天气、计算器、写文档、文生图、语音识别、语音合成）

## 安装
### 客户端

### 服务端
```
pip install -r requirements.txt
uvicorn main.py
```

## TODO 
OCR
天气
计算器
写文档
文生图
语音识别
语音合成