# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : sentence_transformers_embed.py
@time    : 2026/1/15 15:43
@desc    : 使用sentence_transformers进行框架下载bge-m3模型进行向量化
-----------------------------------------------------------------------
"""

from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    print("sentence_transformers_embed...")

    model = SentenceTransformer("/Users/yangguangyuan/QuantLib/models/hf_mirror/embedding/bge-m3")
    sentences = [
        "That is a happy person",
        "That is a happy dog",
        "That is a very happy person",
        "Today is a sunny day"
    ]
    embeddings = model.encode(sentences)
    print(embeddings)

    similarities = model.similarity(embeddings, embeddings)
    print(similarities.shape)

