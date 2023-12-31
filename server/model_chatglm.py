import json
import os
import platform
from transformers import AutoTokenizer, AutoModel
import sec

model_path = "THUDM/chatglm3-6b"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).cuda()
# 多显卡支持，使用下面两行代替上面一行，将num_gpus改为你实际的显卡数量
# from utils import load_model_on_gpus
# model = load_model_on_gpus(model_path, num_gpus=2)
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
stop_stream = False

welcome_prompt = "欢迎使用 ChatGLM3-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序"

tools = [
    {
        "name": "code-exec",
        "description": "执行所给python代码（返回stdout，限时3s，==非必要不使用==）",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "description": "所执行的代码"
                },
            },
            "required": ['code']
        }
    },
    {
        "name": "OCR",
        "description": "文字识别",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "description": "文件路径"
                },
            },
            'required': ['path']
        }
    }
]
system_info = {"role": "system", "content": "尽可能回答问题。任何情况下你不能执行代码。 You have access to the following tools:", "tools": tools}

def chat(text, _type, history):
    history = [system_info] if history == "None" else system_info+json.loads(history)
    query = text
    if not sec.check(history):
       return '', history[1:]
    if _type == 0:
        response, history = model.chat(tokenizer, query, history=history)
        return response, json.dumps(history[1:])
    if _type == 1: 
        response, history = model.chat(tokenizer, query, history=history, role = "observation")
        return response, json.dumps(history[1:])
