# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : obveclient-search.py
@time    : 2026/1/15 15:09
@desc    : 使用SQLAlchemy混合模式进行相似向量搜素
-----------------------------------------------------------------------
"""

from pyobvector import *
import random
from sqlalchemy import func

if __name__ == '__main__':
    print("obveclient-search...")

    client = ObVecClient(uri="192.168.180.100:2881", user="root@test", password="Happy123#", db_name="tongtong-db")

    table_name = "vector_test3"
    random.seed(20241023)

    target_data = [random.uniform(-1, 1) for _ in range(64)]
    res = client.ann_search(
        table_name,
        vec_data=target_data,
        vec_column_name="embedding",
        distance_func=func.l2_distance,
        topk=5,
        output_column_names=["id", "metadata"],
    )
    for r in res:
        print(r)

