import csv
import pandas as pd

class H1bDataReader:

    df = None
    input_file = None
    def __init__(self, input_file, attr_list = {}):
        self.df = pd.read_csv(input_file, low_memory = False)
        self.input_file = input_file
        self.df = self.df.filter(attr_list.keys())
        for attr in attr_list.items():
            if attr[1] is not None:
                self.df = self.df[self.df[attr[0]] == attr[1]]

    def write_to_csv(self, path):
        self.df.to_csv(path, index = False)

    def attr_operator(self, attr, oper = "SUM"):
        unique_attrs = self.df[attr].unique()
        # print(unique_attrs)

        if oper == "SUM":
            rtn = self.df[attr].reset_index(drop=True).value_counts().to_dict()
            print(rtn)
            return rtn

    def state_preprocess(self):
        state_list = []
        with open("../../data/state_abbr.csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state_list.append((row["State"], row["Code"]))


        for state in state_list:
            self.df["WORKSITE_STATE"].replace(state[1], state[0], inplace = True)

        self.df['WORKSITE_STATE'] = self.df['WORKSITE_STATE'].str.title()

if __name__ == "__main__":
    attr_list = {\
        "CASE_NUMBER": None,
        "CASE_STATUS": None,
        "SOC_NAME": None,
        "FULL_TIME_POSITION": None,
        "WORKSITE_STATE": None
    }
    df_reader = H1bDataReader("../../data/h1b_data_2019.csv", attr_list = attr_list)
    df_reader.state_preprocess()
    df_reader.attr_operator("CASE_STATUS")
    df_reader.attr_operator("WORKSITE_STATE")

