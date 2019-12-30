from df_heatmap import df_heatmap
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import pdb

# data = load_breast_cancer().data
# input_df = pd.DataFrame(data, columns=load_breast_cancer().feature_names)
# target_df = input_df[load_breast_cancer().feature_names[0:6]].corr().astype(float).round(3)

data = load_iris().data
input_df = pd.DataFrame(data, columns=load_iris().feature_names)
input_df.columns = ['a','b','c','d']

target_df = input_df.corr().astype(float).round(3)

df_heatmap(data=target_df)._set_color(color_target='background')

# df = pd.DataFrame([1,2.01,3.23])
