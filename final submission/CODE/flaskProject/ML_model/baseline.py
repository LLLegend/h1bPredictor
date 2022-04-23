import pandas as pd
import numpy as np
import os
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn import metrics
import warnings
pd.set_option('display.max_columns', 100)
warnings.filterwarnings('ignore')

n_fold = 10

train_path = "../../data/train.csv"
test_path = "../../data/test.csv"

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
target = "CASE_STATUS"
features = [x for x in train.columns if x not in [target]]
cat_features = ["EMPLOYER_NAME", "EMPLOYER_BUSINESS_DBA", "SOC_NAME", "NAICS_CODE", "FULL_TIME_POSITION",
                "PW_UNIT_OF_PAY", "WAGE_UNIT_OF_PAY", "WORKSITE_CITY", "WORKSITE_STATE"]

params = {
    'n_estimators': 100,
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'early_stopping_rounds': 10,
    'learning_rate': 0.05,
    'metric': "binary_logloss",
   # "min_data_in_leaf": 100,
   #  'num_leaves': 55, 
   #  "max_depth": 8,
   # "lambda_l1": 0.1,
   # 'feature_fraction': 0.8,
    "verbosity": -1,
   # "bagging_fraction": 0.9,
   # "lambda_l2": 0.1
}
print(params)

fold = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=42)

X_train = train[features].copy()
y_train = train[target]
X_train[cat_features] = X_train[cat_features].astype('category')

X_test = test[features].copy()
y_test = test[target]
X_test[cat_features] = X_test[cat_features].astype('category')

models = []
oof = np.zeros((len(X_train), ))
pred = np.zeros((len(X_test), ))
for index, (train_idx, val_idx) in enumerate(fold.split(X_train, y_train)):
    train_set = lgb.Dataset(X_train.iloc[train_idx], y_train.iloc[train_idx])
    val_set = lgb.Dataset(X_train.iloc[val_idx], y_train.iloc[val_idx])
 
    model = lgb.train(params, train_set, valid_sets=[train_set, val_set], verbose_eval=50)
    models.append(model)

    val_pred = model.predict(X_train.iloc[val_idx])
    oof[val_idx] = val_pred
    val_y = y_train.iloc[val_idx]
    val_pred[val_pred < 0.5] = 0
    val_pred[val_pred >= 0.5] = 1
    print(index, 'acc', metrics.accuracy_score(val_y, val_pred))

    test_pred = model.predict(X_test)
    pred += test_pred / n_fold

oof[oof < 0.5] = 0
oof[oof >= 0.5] = 1

pred[pred < 0.5] = 0
pred[pred >= 0.5] = 1

print("acc for training data: ", metrics.accuracy_score(y_train, oof))
print("acc for testing data: ", metrics.accuracy_score(y_test, pred))

print("recall for training data: ", metrics.recall_score(y_train, oof))
print("recall for testing data: ", metrics.recall_score(y_test, pred))

print("f1-score for training data: ", metrics.f1_score(y_train, oof))
print("f1-score for testing data: ", metrics.f1_score(y_test, pred))

if not os.path.exists("models/"):
    os.mkdir("models")

for i in range(len(models)):
    models[i].save_model("models/lgb_model_{}.txt".format(i))

