import numpy as np
import pandas as pd

# #Jupyter Notebookの出力を小数点以下3桁に抑える
# %precision 3

#Dataframeの出力を小数点以下3桁の抑える
pd.set_option('precision', 3)

df = pd.read_csv('./data/ch2_scores_em.csv', index_col='生徒番号')

#dfの最初の5行を表示
df.head()