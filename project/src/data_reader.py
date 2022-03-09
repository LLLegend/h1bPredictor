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


if __name__ == "__main__":
    attr_list = {\
        "CASE_NUMBER": None,
        "CASE_STATUS": None,
        "JOB_TITLE": None,
        "SOC_TITLE": None,
        "FULL_TIME_POSITION": None,
    }
    read_raw_data("../../data/H-1B_Disclosure_Data_FY2019.csv", attr_list = attr_list, write_csv = True)
