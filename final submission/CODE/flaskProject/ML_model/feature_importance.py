import numpy as np
import pandas as pd
import lightgbm as lgb

models = []
for i in range(10):
    models.append(lgb.Booster(model_file="models/lgb_model_{}.txt".format(i)))

ret = []
for index, model in enumerate(models):
    df = pd.DataFrame()
    df['name'] = model.feature_name()
    df['score'] = model.feature_importance()
    df['fold'] = index
    ret.append(df)

df = pd.concat(ret)

df = df.groupby('name', as_index=False)['score'].mean()
df = df.sort_values(['score'], ascending=False)
df.to_csv("../../data/feature_importance.csv", index=None)
