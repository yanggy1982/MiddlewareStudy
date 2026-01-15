# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : obveclient-create-collection.py
@time    : 2026/1/15 14:41
@desc    : 使用SQLAlchemy混合模式创建集合
-----------------------------------------------------------------------
"""

from pyobvector import *
from sqlalchemy import Column, Integer, JSON

if __name__ == '__main__':
    print("obveclient-create-collection...")

    client = ObVecClient(uri="192.168.180.100:2881", user="root@test",password="Happy123#", db_name="tongtong-db")

    cols = [
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("embedding", VECTOR(64)),
        Column("metadata", JSON),
    ]
    table_name = "vector_test3"
    client.create_table(table_name, columns=cols)
    print(f"Table {table_name} created")
    client.create_index(
        table_name,
        is_vec_index=True,
        index_name="embedding_idx",
        column_names=["embedding"],
        vidx_params="distance=l2, type=hnsw, lib=vsag",  # m=16, ef_construction=256
    )
    print(f"Index {table_name}.embedding_idx created")


