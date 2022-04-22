import numpy as np
import pandas as pd
import lightgbm as lgb


def predict(x):
    """
    :param x: a list of value of features
              such as ["TEKSHAPERS, INC.", "", "Marketing Managers", "45411.0", "Y",
                       "Year", "Year", "Seattle", "WA", 1.0, 125171.0, 137400.0]
              values should meet a fixed order
              values can be a list, which means the input pass multiple cases

    :return: list of the probability
    """
    dict_ = {"EMPLOYER_NAME": None,
             "EMPLOYER_BUSINESS_DBA": None,
             "SOC_NAME": None,
             "NAICS_CODE": None,
             "FULL_TIME_POSITION": None,
             "PW_UNIT_OF_PAY": None,
             "WAGE_UNIT_OF_PAY": None,
             "WORKSITE_CITY": None,
             "WORKSITE_STATE": None,
             "TOTAL_WORKERS": None,
             "PREVAILING_WAGE": None,
             "WAGE_RATE_OF_PAY_FROM": None}
    cat_features = ["EMPLOYER_NAME", "EMPLOYER_BUSINESS_DBA", "SOC_NAME", "NAICS_CODE", "FULL_TIME_POSITION",
                    "PW_UNIT_OF_PAY", "WAGE_UNIT_OF_PAY", "WORKSITE_CITY", "WORKSITE_STATE"]
    for i, j in enumerate(dict_.keys()):
        dict_[j] = x[i]
    df = pd.DataFrame(dict_, index=[0])
    df[cat_features] = df[cat_features].astype("category")
    prob = 0
    for k in range(10):
        model = lgb.Booster(model_file="models/lgb_model_{}.txt".format(k))
        prob += model.predict(df) / 10
    return prob

