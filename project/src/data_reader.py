import csv
import pandas as pd


def read_raw_data(input_file, attr_list = {}, write_csv = False):

    df = pd.read_csv(input_file, low_memory = False)
    print(df.shape)
    df = df[df["VISA_CLASS"] == "H-1B"]
    df = df.filter(attr_list.keys())

    for attr in attr_list.items():
        if attr[1] is not None:
            df = df[df[attr[0]] == attr[1]]

    print(df.shape)

    if write_csv:
        df.to_csv(input_file + "_new.csv", index = False)

    return df.shape

def read_cleaned_data(input_file, attr_list = {}):

    df = pd.read_csv(input_file, low_memory = False)

    df = df.filter(attr_list.keys())
    for attr in attr_list.items():
        if attr[1] is not None:
            df = df[df[attr[0]] == attr[1]]

    return df

def attr_operator(df, attr, oper = "SUM"):
    unique_attrs = df[attr].unique()
    # print(unique_attrs)

    if oper == "SUM":
        rtn = df[attr].reset_index(drop=True).value_counts().to_dict()
        # print(rtn)
        return rtn

def state_preprocess(df):
    state_list = []
    with open("../../data/state_abbr.csv", newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            state_list.append((row["State"], row["Code"]))


    for state in state_list:
        df["WORKSITE_STATE"].replace(state[1], state[0], inplace = True)

    df['WORKSITE_STATE'] = df['WORKSITE_STATE'].str.title()
    return df

if __name__ == "__main__":
    attr_list = {\
        "CASE_NUMBER": None,
        "CASE_STATUS": None,
        "SOC_NAME": None,
        "FULL_TIME_POSITION": None,
        "WORKSITE_STATE": None
    }
    df = read_cleaned_data("../../data/h1b_data_2019.csv", attr_list = attr_list)
    state_preprocess(df)
    attr_operator(df, "CASE_STATUS")
    attr_operator(df, "WORKSITE_STATE")

