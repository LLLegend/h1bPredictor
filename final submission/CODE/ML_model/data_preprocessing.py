import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import re

def str2num(x):
    x = re.findall("(\d+)", str(x))
    x.reverse()
    a = 0
    for j in range(len(x)):
        if j == 0:
            a += int(x[j]) * 0.1
        else:
            a += int(x[j]) * 1000 ** (j - 1)
    return a

def cleaning(a):
    a = str(a)
    a = a.replace(" ", "")
    a = re.sub('\W*', '', a)
    return a

def data_preprocessing(data):
    selected_features = ["CASE_STATUS", "EMPLOYER_NAME", "EMPLOYER_BUSINESS_DBA", "SOC_NAME",
                         "NAICS_CODE", "FULL_TIME_POSITION",
                         "PW_UNIT_OF_PAY", "WAGE_UNIT_OF_PAY", "WORKSITE_CITY", "WORKSITE_STATE",
                         "TOTAL_WORKERS", "PREVAILING_WAGE", "WAGE_RATE_OF_PAY_FROM"]
    # drop_columns = ["CASE_NUMBER", "RECEIVED_DATE", "DECISION_DATE"]
    # data.drop(drop_columns, axis=1, inplace=True)

    data = data[selected_features]

    data["CASE_STATUS"] = data["CASE_STATUS"].replace("CERTIFIED", 1)
    data["CASE_STATUS"] = data["CASE_STATUS"].replace("Certified", 1)
    data["CASE_STATUS"] = data["CASE_STATUS"].replace("Certifi", 1)

    data["CASE_STATUS"] = data["CASE_STATUS"].replace("CERTIFIED-WITHDRAWN", 1)
    data["CASE_STATUS"] = data["CASE_STATUS"].replace("Certified - Withdrawn", 1)

    data["CASE_STATUS"] = data["CASE_STATUS"].replace("WITHDRAWN", 0)
    data["CASE_STATUS"] = data["CASE_STATUS"].replace("Withdrawn", 0)

    data["CASE_STATUS"] = data["CASE_STATUS"].replace("DENIED", 0)
    data["CASE_STATUS"] = data["CASE_STATUS"].replace("Denied", 0)

    data["PREVAILING_WAGE"] = data["PREVAILING_WAGE"].apply(str2num)
    data["WAGE_RATE_OF_PAY_FROM"] = data["WAGE_RATE_OF_PAY_FROM"].apply(str2num)

    # data["PW_WAGE_LEVEL"] = data["PW_WAGE_LEVEL"].replace("I", 1)
    # data["PW_WAGE_LEVEL"] = data["PW_WAGE_LEVEL"].replace("II", 2)
    # data["PW_WAGE_LEVEL"] = data["PW_WAGE_LEVEL"].replace("III", 3)
    # data["PW_WAGE_LEVEL"] = data["PW_WAGE_LEVEL"].replace("IV", 4)
    # data["PW_WAGE_LEVEL"] = data["PW_WAGE_LEVEL"].replace("N/A", np.nan)

    data["EMPLOYER_NAME"] = data["EMPLOYER_NAME"].apply(cleaning)
    data["EMPLOYER_NAME"] = data["EMPLOYER_NAME"].apply(lambda x: x.replace("LLC", ""))
    data["EMPLOYER_NAME"] = data["EMPLOYER_NAME"].apply(lambda x: x.replace("INC", ""))

    # data["SOC_NAME"] = data["SOC_NAME"].apply(cleaning)
    # data["SOC_NAME"] = data["SOC_NAME"].replace("\..*$", "", regex=True)
    data["WORKSITE_CITY"] = data["WORKSITE_CITY"].apply(cleaning)

    return data

split_size = 0.7
target_value = "CASE_STATUS"
seed = 6242
years = ["2017", "2018", "2019", "2020", "2021"]
train_path = "../../data/train.csv"
test_path = "../../data/test.csv"

for i in range(len(years)):
    if i == 0:
        df_1 = pd.read_csv("../../data/h1b_data_{}_new.csv".format(years[i]))
        df_1 = data_preprocessing(df_1)
    else:
        df_2 = pd.read_csv("../../data/h1b_data_{}_new.csv".format(years[i]))
        df_2 = data_preprocessing(df_2)
        df_1 = pd.concat([df_1, df_2], axis=0)

features = [i for i in df_1.columns if i != target_value]

X_train, X_test, y_train, y_test = train_test_split(df_1[features], df_1[target_value])

data_train = pd.concat([X_train, y_train], axis=1)
data_test = pd.concat([X_test, y_test], axis=1)

data_train.to_csv(train_path, index=False)
data_test.to_csv(test_path, index=False)
