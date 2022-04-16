import csv
import pandas as pd
import numpy as np

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

    def get_df_shape(self):
        return self.df.shape

    def attr_operator(self, attr, oper = "SUM", head = 0, others = False, filter_dict = {}, drop_cases_val = 0):
        # unique_attrs = self.df[attr].unique()
        # print(unique_attrs)

        tmp_df = self.df

        for col_key, col_dict in filter_dict.items():
            if "EQUAL" in col_dict:
                tmp_df = tmp_df[tmp_df[col_key] == col_dict["EQUAL"]]
            if "LESS" in col_dict:
                tmp_df = tmp_df[tmp_df[col_key] <= col_dict["LESS"]]
            if "GREATER" in col_dict:
                tmp_df = tmp_df[tmp_df[col_key] >= col_dict["GREATER"]]

        if oper == "SUM":
            opered_data = tmp_df[attr].reset_index(drop=True).value_counts()
            opered_data = opered_data[opered_data > drop_cases_val]

        if oper == "RATIO":
            tmp_df = tmp_df.replace({"CASE_STATUS": ["CERTIFIED", "CERTIFIED-WITHDRAWN"]}, 1)
            tmp_df = tmp_df.replace({"CASE_STATUS": ["DENIED", "WITHDRAWN"]}, 0)
            tmp_df = tmp_df.groupby(attr).agg({"CASE_STATUS" : ["sum", "count"]})
            tmp_df.columns = tmp_df.columns.droplevel(0)
            tmp_df = tmp_df[tmp_df["count"] > drop_cases_val]

            opered_data = tmp_df["sum"] / tmp_df["count"]
            opered_data = opered_data.sort_values(ascending=False)


        rtn = opered_data
        if head > 0:
            rtn = opered_data.head(head)

        rtn_dict = rtn.to_dict()

        if others:
            tail = opered_data.shape[0] - head
            data_tail = opered_data.tail(tail)
            rtn_dict["OTHER"] = data_tail.sum()

        print(rtn_dict)
        return rtn_dict

    def salary_range(self, split = 20, max_bar = 350000):
        salary_app_num_dict = {}
        salary_pass_rate_dict = {}

        salary_part_down = self.df[self.df["WAGE_RATE_OF_PAY_FROM"] <= max_bar]
        salary_part_up = self.df[self.df["WAGE_RATE_OF_PAY_FROM"] > max_bar]
        # salary_min = salary_part_down["WAGE_RATE_OF_PAY_FROM"].min()
        # salary_max = salary_part_down["WAGE_RATE_OF_PAY_FROM"].max()

        salary_list = np.linspace(0, max_bar, split, endpoint=False)


        for i in range(split):
            salary = salary_list[i]
            tmp_df = salary_part_down[salary_part_down["WAGE_RATE_OF_PAY_FROM"] >= salary]
            if i < split - 1:
                tmp_df = tmp_df[tmp_df["WAGE_RATE_OF_PAY_FROM"] < salary_list[i + 1]]
            salary_app_num_dict[salary] = tmp_df.shape[0]
            salary_pass_rate_dict[salary] = 0
            if tmp_df.shape[0] > 0:
                salary_pass_rate_dict[salary] = (tmp_df[tmp_df["CASE_STATUS"] == "CERTIFIED"].shape[0] + \
                                                tmp_df[tmp_df["CASE_STATUS"] == "CERTIFIED-WITHDRAWN"].shape[0]) / tmp_df.shape[0]

        salary_app_num_dict[max_bar] = salary_part_up.shape[0]
        salary_pass_rate_dict[max_bar] = 0
        if salary_part_up.shape[0] > 0:
            salary_pass_rate_dict[max_bar] = (salary_part_up[salary_part_up["CASE_STATUS"] == "CERTIFIED"].shape[0] + \
                                            salary_part_up[salary_part_up["CASE_STATUS"] == "CERTIFIED-WITHDRAWN"].shape[0]) / salary_part_up.shape[0]

        print(salary_app_num_dict, salary_pass_rate_dict)
        return salary_app_num_dict, salary_pass_rate_dict



    def state_preprocess(self):
        state_list = []
        with open("../../data/state_abbr.csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state_list.append((row["State"], row["Code"]))


        for state in state_list:
            self.df["WORKSITE_STATE"].replace(state[1], state[0], inplace = True)

        self.df['WORKSITE_STATE'] = self.df['WORKSITE_STATE'].str.title()

    def salary_preprocess(self):
        self.df["WAGE_RATE_OF_PAY_FROM"].replace('[\$,]', '', inplace = True, regex=True)
        # self.df.dropna(subset = ["WAGE_RATE_OF_PAY_FROM"], inplace = True)
        self.df = self.df.astype({"WAGE_RATE_OF_PAY_FROM": float})

    def casestate_preprocess(self):
        self.df["CASE_STATUS"].replace("Certifi", "CERTIFIED", inplace = True)
        self.df["CASE_STATUS"] = self.df["CASE_STATUS"].str.replace(' ', '').str.upper()


if __name__ == "__main__":
    attr_list = {\
        "CASE_NUMBER": None,
        "CASE_STATUS": None,
        "SOC_NAME": None,
        "FULL_TIME_POSITION": None,
        "WORKSITE_STATE": None,
        "EMPLOYER_NAME": None,
        "WAGE_RATE_OF_PAY_FROM": None,
        "WAGE_UNIT_OF_PAY": "Year"
    }
    df_reader = H1bDataReader("../../data/h1b_data_2017.csv", attr_list = attr_list)
    df_reader.state_preprocess()
    df_reader.salary_preprocess()
    df_reader.casestate_preprocess()
    df_reader.attr_operator("CASE_STATUS")
    df_reader.attr_operator("WORKSITE_STATE")
    df_reader.attr_operator("EMPLOYER_NAME", head = 10)
    df_reader.attr_operator("SOC_NAME", head = 10)
    df_reader.salary_range()
    df_reader.attr_operator("SOC_NAME", head = 10, filter_dict = {"WAGE_RATE_OF_PAY_FROM": {"GREATER": 100000, "LESS": 200000}})
    df_reader.attr_operator("SOC_NAME", oper = "RATIO", head = 10, drop_cases_val = 1000)

