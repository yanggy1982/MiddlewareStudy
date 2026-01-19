# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : ollama_embed_demo2.py
@time    : 2026/1/15 17:35
@desc    : 通过python sdk调用ollama向量模型进行向量化
-----------------------------------------------------------------------
"""

import ollama

if __name__ == '__main__':
    print("ollama_embed_demo21...")

    texts = ["第一个句子", "第二个句子"]
    embeddings = ollama.embed(model="bge-m3", input=texts)['embeddings']
    print(embeddings)
