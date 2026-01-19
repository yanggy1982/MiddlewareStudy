# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : ollama_embed_demo1.py
@time    : 2026/1/15 17:33
@desc    : 通过API调用ollama向量模型进行向量化
-----------------------------------------------------------------------
"""

import requests

def get_embedding(text: str) -> list:
    """使用 Ollama 的 HTTP API 获取文本嵌入"""
    response = requests.post(
    'http://localhost:11434/api/embeddings',
    json={
        'model': 'bge-m3',
        'prompt': text
    }
    )
    return response.json()['embedding']

if __name__ == '__main__':
    print("ollama_embed_demo1...")

    # 示例使用
    text = "这是一个示例文本"
    embedding = get_embedding(text)
    print(embedding)

