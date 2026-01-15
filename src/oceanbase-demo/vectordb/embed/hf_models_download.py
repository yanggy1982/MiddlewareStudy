# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : hf_models_download.py
@time    : 2026/1/15 16:47
@desc    : 模型下载
-----------------------------------------------------------------------
"""

from huggingface_hub import snapshot_download
import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # 核心配置

if __name__ == '__main__':
    print("hf_models_download...")

    snapshot_download(repo_id="BAAI/bge-m3",local_dir="/Users/yangguangyuan/QuantLib/models/hf_mirror/embedding")
