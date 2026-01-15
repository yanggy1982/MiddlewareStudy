# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : obvector-search-demo1.py
@time    : 2026/1/14 10:16
@desc    : 向量检索
-----------------------------------------------------------------------
"""

from pyobvector import *
import random

if __name__ == '__main__':
    print("obvector-search-demo1...")

    # 创建客户端
    client = MilvusLikeClient(uri="192.168.180.100:2881", user="root@test", password="Happy123#", db_name="tongtong-db")

    table_name = "vector_search"

    target_data = [random.uniform(-1, 1) for _ in range(64)]
    res = client.search(
        collection_name=table_name,
        data=target_data,
        anns_field="embedding",
        limit=5,
        output_fields=["id", "metadata"],
    )
    print(res)