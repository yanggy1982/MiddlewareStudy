# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : obveclient-insert-data.py
@time    : 2026/1/15 14:59
@desc    : 使用SQLAlchemy混合模式批量插入数据
-----------------------------------------------------------------------
"""

from pyobvector import *
import random

if __name__ == '__main__':
    print("obveclient-insert-data...")

    client = ObVecClient(uri="192.168.180.100:2881", user="root@test", password="Happy123#", db_name="tongtong-db")

    table_name = "vector_test3"
    random.seed(20241023)

    batch_size = 100
    batch = []
    for i in range(1000):
        batch.append(
            {
                "embedding": [random.uniform(-1, 1) for _ in range(64)],
                "metadata": {"idx": i},
            }
        )
        if len(batch) == batch_size:
            client.insert(table_name, data=batch)
            batch = []

    if len(batch) > 0:
        client.insert(table_name, data=batch)


