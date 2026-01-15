# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : milvuslikeclient-create-collection.py
@time    : 2026/1/13 14:51
@desc    : 创建集合
-----------------------------------------------------------------------
"""

from pyobvector import *

if __name__ == '__main__':
    print("ob-vector-demo1...")

    # 创建客户端
    client = MilvusLikeClient(uri="192.168.180.100:2881", user="root@test",password="Happy123#", db_name="tongtong-db")

    fields = [
        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            is_primary=True,
            auto_id=True,
        ),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=64),
        FieldSchema(name="metadata", dtype=DataType.JSON),
    ]

    index_params = MilvusLikeClient.prepare_index_params()
    index_params.add_index(
        field_name="embedding",
        index_name="embedding_idx",
        index_type=VecIndexType.HNSW,
        distance="l2",
        m=16,
        ef_construction=256,
    )

    schema = CollectionSchema(fields)
    table_name = "vector_search"
    client.create_collection(table_name, schema=schema, index_params=index_params)



