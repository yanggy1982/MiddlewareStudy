# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : huggingface_transformers_embed.py
@time    : 2026/1/15 16:11
@desc    : 使用HuggingFace Transformers进行框架下载bge-m3模型进行向量化
-----------------------------------------------------------------------
"""

from transformers import AutoTokenizer, AutoModel
import torch

if __name__ == '__main__':
    print("huggingface_transformers_embed...")

    # 加载模型和分词器
    tokenizer = AutoTokenizer.from_pretrained("/Users/yangguangyuan/QuantLib/models/hf_mirror/embedding/bge-m3")
    model = AutoModel.from_pretrained("/Users/yangguangyuan/QuantLib/models/hf_mirror/embedding/bge-m3")

    # 准备输入
    texts = ["这是示例文本"]
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

    # 生成嵌入
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, 0]  # 使用 [CLS] token 的输出
        print(embeddings)
        # tensor([[-1.4136,  0.7477, -0.9914,  ...,  0.0937, -0.0362, -0.1650]])
    print(embeddings.shape)
