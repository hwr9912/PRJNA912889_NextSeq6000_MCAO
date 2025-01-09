# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:36:54 2024

@author: William_Han
"""
#%% 数据读取
import scanpy as sc
import pandas as pd
import functions as utl

targets = pd.DataFrame({
    "sample_id": [f"SRR263317{i}" for i in ["08", "09", "10", "11"]],
    "group": ["S12h", "S3h", "sham", "S3d"]
    })
targets.loc[:,"filedir"] =[f"data/{path}_filtered_feature_bc_matrix.h5"
                           for path in targets.loc[:,"sample_id"]]
targets.to_hdf("data/PRJNA912889_targets.h5", key="df", mode="w")

# 分别读取文件
PRJNA912889_data = [utl.read_sc_data(path) for path in targets["filedir"]]
for i in range(targets):
    PRJNA912889_data.vars