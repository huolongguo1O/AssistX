import os
import platform
from transformers import AutoTokenizer, AutoModel

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
        "description": "执行所给python代码（返回stdout）",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "description": "所执行的代码"
                },
            },
            "required": ['code']
        }
    }
]
system_info = {"role": "system", "content": "Answer the following questions as best as you can. You have access to the following tools:", "tools": tools}

def chat(text, _type, history):
    history = [system_info] if history == "None" else history
    query = text
    if _type == 0:
        response, history = model.chat(tokenizer, query, history=history)
        return response, history
    if _type == 1: 
        response, history = model.chat(tokenizer, query, history=history, role = "observation")
        return response, history
