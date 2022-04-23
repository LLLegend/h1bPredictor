from flask import Flask
import flask_restful as restful
import data_reader as util
import pandas as pd
from ML_model import predictor
from flask_restful import reqparse
from ML_model import data_preprocessing

parser = reqparse.RequestParser()
parser.add_argument('employer', type=str)
parser.add_argument('jobTitle', type=str)
parser.add_argument('city', type=str)
parser.add_argument('state', type=str)
parser.add_argument('wage', type=float)


app = Flask(__name__)
api = restful.Api(app)


@app.route("/download/<filepath>", methods=['GET'])
def download_file(filepath):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file(filepath)



attr_list = { \
    "CASE_NUMBER": None,
    "CASE_STATUS": None,
    "SOC_NAME": None,
    "FULL_TIME_POSITION": None,
    "WORKSITE_STATE": None,
    "EMPLOYER_NAME": None,
    "WAGE_RATE_OF_PAY_FROM": None,
    "WAGE_UNIT_OF_PAY": "Year",
    "WORKSITE_CITY": None,
}
df_reader_2017 = util.H1bDataReader("../data/h1b_data_2017_new.csv", attr_list=attr_list)
df_reader_2018 = util.H1bDataReader("../data/h1b_data_2018_new.csv", attr_list=attr_list)
df_reader_2019 = util.H1bDataReader("../data/h1b_data_2019_new.csv", attr_list=attr_list)
df_reader_2020 = util.H1bDataReader("../data/h1b_data_2020_new.csv", attr_list=attr_list)
df_reader_2021 = util.H1bDataReader("../data/h1b_data_2021_new.csv", attr_list=attr_list)
# df_reader_2017.state_preprocess()
# df_reader_2018.state_preprocess()
# df_reader_2019.state_preprocess()
# df_reader_2020.state_preprocess()
# df_reader_2021.state_preprocess()
# df_reader_2017.salary_preprocess()
# df_reader_2018.salary_preprocess()
# df_reader_2019.salary_preprocess()
# df_reader_2020.salary_preprocess()
# df_reader_2021.salary_preprocess()
# df_reader_2017.casestate_preprocess()
# df_reader_2018.casestate_preprocess()
# df_reader_2019.casestate_preprocess()
# df_reader_2020.casestate_preprocess()
# df_reader_2021.casestate_preprocess()
# df_reader_2017.soc_preprocess()
# df_reader_2018.soc_preprocess()
# df_reader_2019.soc_preprocess()
# df_reader_2020.soc_preprocess()
# df_reader_2021.soc_preprocess()
# df_reader_2017.city_preprocess()
# df_reader_2018.city_preprocess()
# df_reader_2019.city_preprocess()
# df_reader_2020.city_preprocess()
# df_reader_2021.city_preprocess()
# df_reader_2017.employer_preprocess()
# df_reader_2018.employer_preprocess()
# df_reader_2019.employer_preprocess()
# df_reader_2020.employer_preprocess()
# df_reader_2021.employer_preprocess()

# case_status
case_status_17 = df_reader_2017.attr_operator("CASE_STATUS")
case_status_18 = df_reader_2018.attr_operator("CASE_STATUS")
case_status_19 = df_reader_2019.attr_operator("CASE_STATUS")
case_status_20 = df_reader_2020.attr_operator("CASE_STATUS")
case_status_21 = df_reader_2021.attr_operator("CASE_STATUS")

# worksite_state
worksite_state_17 = df_reader_2017.attr_operator("WORKSITE_STATE")
worksite_state_18 = df_reader_2018.attr_operator("WORKSITE_STATE")
worksite_state_19 = df_reader_2019.attr_operator("WORKSITE_STATE")
worksite_state_20 = df_reader_2020.attr_operator("WORKSITE_STATE")
worksite_state_21 = df_reader_2021.attr_operator("WORKSITE_STATE")

# number of visa applications by employer_name
cases_by_employer_17 = df_reader_2017.attr_operator("EMPLOYER_NAME", head=10)
cases_by_employer_18 = df_reader_2018.attr_operator("EMPLOYER_NAME", head=10)
cases_by_employer_19 = df_reader_2019.attr_operator("EMPLOYER_NAME", head=10)
cases_by_employer_20 = df_reader_2020.attr_operator("EMPLOYER_NAME", head=10)
cases_by_employer_21 = df_reader_2021.attr_operator("EMPLOYER_NAME", head=10)

# number of visa applications by soc_name
cases_by_job_title_17 = df_reader_2017.attr_operator("SOC_NAME", head=10)
cases_by_job_title_18 = df_reader_2018.attr_operator("SOC_NAME", head=10)
cases_by_job_title_19 = df_reader_2019.attr_operator("SOC_NAME", head=10)
cases_by_job_title_20 = df_reader_2020.attr_operator("SOC_NAME", head=10)
cases_by_job_title_21 = df_reader_2021.attr_operator("SOC_NAME", head=10)

df_shape_17 = df_reader_2017.get_df_shape()[0]
df_shape_18 = df_reader_2018.get_df_shape()[0]
df_shape_19 = df_reader_2019.get_df_shape()[0]
df_shape_20 = df_reader_2020.get_df_shape()[0]
df_shape_21 = df_reader_2021.get_df_shape()[0]

# certified rate
df_cert_rate_17 = (case_status_17["CERTIFIED"] + case_status_17["CERTIFIED-WITHDRAWN"]) / df_shape_17
df_cert_rate_18 = (case_status_18["CERTIFIED"] + case_status_18["CERTIFIED-WITHDRAWN"]) / df_shape_18
df_cert_rate_19 = (case_status_19["CERTIFIED"] + case_status_19["CERTIFIED-WITHDRAWN"]) / df_shape_19
df_cert_rate_20 = (case_status_20["CERTIFIED"] + case_status_20["CERTIFIED-WITHDRAWN"]) / df_shape_20
df_cert_rate_21 = (case_status_21["CERTIFIED"] + case_status_21["CERTIFIED-WITHDRAWN"]) / df_shape_21

employer_list_17 = df_reader_2017.attr_operator("EMPLOYER_NAME")
employer_list_18 = df_reader_2018.attr_operator("EMPLOYER_NAME")
employer_list_19 = df_reader_2018.attr_operator("EMPLOYER_NAME")
employer_list_20 = df_reader_2018.attr_operator("EMPLOYER_NAME")
employer_list_21 = df_reader_2018.attr_operator("EMPLOYER_NAME")
employer_set = set()
employer_set.update(tuple(employer_list_17))
employer_set.update(tuple(employer_list_18))
employer_set.update(tuple(employer_list_19))
employer_set.update(tuple(employer_list_20))
employer_set.update(tuple(employer_list_21))


job_list_17 = df_reader_2017.attr_operator("SOC_NAME", drop_cases_val=10)
job_list_18 = df_reader_2018.attr_operator("SOC_NAME", drop_cases_val=10)
job_list_19 = df_reader_2019.attr_operator("SOC_NAME", drop_cases_val=10)
job_list_20 = df_reader_2020.attr_operator("SOC_NAME", drop_cases_val=10)
job_list_21 = df_reader_2021.attr_operator("SOC_NAME", drop_cases_val=10)
job_set = set()
job_set.update(job_list_17)
job_set.update(job_list_18)
job_set.update(job_list_19)
job_set.update(job_list_20)
job_set.update(job_list_21)

city_list_17 = df_reader_2017.attr_operator("WORKSITE_CITY")
city_list_18 = df_reader_2018.attr_operator("WORKSITE_CITY")
city_list_19 = df_reader_2019.attr_operator("WORKSITE_CITY")
city_list_20 = df_reader_2020.attr_operator("WORKSITE_CITY")
city_list_21 = df_reader_2021.attr_operator("WORKSITE_CITY")
city_set = set()
city_set.update(city_list_17)
city_set.update(city_list_18)
city_set.update(city_list_19)
city_set.update(city_list_20)
city_set.update(city_list_21)

state_list_17 = df_reader_2017.attr_operator("WORKSITE_STATE")
state_list_18 = df_reader_2018.attr_operator("WORKSITE_STATE")
state_list_19 = df_reader_2019.attr_operator("WORKSITE_STATE")
state_list_20 = df_reader_2020.attr_operator("WORKSITE_STATE")
state_list_21 = df_reader_2021.attr_operator("WORKSITE_STATE")
state_set = set()
state_set.update(state_list_17)
state_set.update(state_list_18)
state_set.update(state_list_19)
state_set.update(state_list_20)
state_set.update(state_list_21)

class EmployerList(restful.Resource):
    def get(self):
        return list(employer_set)
api.add_resource(EmployerList, '/employer_list')

class JobList(restful.Resource):
    def get(self):
        return list(job_set)
api.add_resource(JobList, '/job_list')

class CityList(restful.Resource):
    def get(self):
        return list(city_set)
api.add_resource(CityList, '/city_list')

class StateList(restful.Resource):
    def get(self):
        return list(state_set)
api.add_resource(StateList, '/state_list')

class CertificationRate(restful.Resource):
    def get(self):
        return {"2017": df_cert_rate_17, "2018": df_cert_rate_18, "2019": df_cert_rate_19, "2020": df_cert_rate_20, "2021": df_cert_rate_21}
api.add_resource(CertificationRate, '/certification_rate')

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'GUNDAM'}
api.add_resource(HelloWorld, '/')


class Trends(restful.Resource):
    def get(self):
        # put application's code here
        return {
            "2017": df_shape_17,
            "2018": df_shape_18,
            "2019": df_shape_19,
            "2020": df_shape_20,
            "2021": df_shape_21,
        }


api.add_resource(Trends, "/trends")


# all possible job titles
class JobTitles(restful.Resource):
    def get(self):
        return job_titles


api.add_resource(JobTitles, "/job_titles")


# return the CertifiedRateByState when user searching by job title
class JobCertifiedRateByState(restful.Resource):
    def get(self, job_title):
        # format
        return {
            "state1": {
                "test": job_title
            },
            "state2": {
                "test2": job_title
            }
        }


api.add_resource(JobCertifiedRateByState, "/job_certified_rate_by_state/<string:job_title>")


# return the case status
class CASE_STATUS(restful.Resource):
    def get(self):
        # format
        return [case_status_17, case_status_18, case_status_19, case_status_20, case_status_21]
api.add_resource(CASE_STATUS, "/case_status")


# return the worksite state
class WORKSITE_STATE(restful.Resource):
    def get(self):
        # format
        return [worksite_state_17, worksite_state_18, worksite_state_19, worksite_state_20, worksite_state_21]
api.add_resource(WORKSITE_STATE, "/worksite_state")


# return the case status
class USTopo(restful.Resource):
    def get(self):
        # format
        return [case_status_17, case_status_18, case_status_19, case_status_20, case_status_21]


api.add_resource(USTopo, "/us_topo")


# return the cases by employer
class CasesByEmployer(restful.Resource):
    def get(self):
        # format
        return [cases_by_employer_17, cases_by_employer_18, cases_by_employer_19, cases_by_employer_20,
                cases_by_employer_21]


api.add_resource(CasesByEmployer, "/cases_by_employer")


# return the cases by job title
class CasesByJobTitle(restful.Resource):
    def get(self):
        # format
        return [cases_by_job_title_17, cases_by_job_title_18, cases_by_job_title_19, cases_by_job_title_20,
                cases_by_job_title_21]


api.add_resource(CasesByJobTitle, "/cases_by_job_title")

salary_range_2017 = df_reader_2017.salary_range(split=10, max_bar=250000)
salary_range_2018 = df_reader_2018.salary_range(split=10, max_bar=250000)
salary_range_2019 = df_reader_2019.salary_range(split=10, max_bar=250000)
salary_range_2020 = df_reader_2020.salary_range(split=10, max_bar=250000)
salary_range_2021 = df_reader_2021.salary_range(split=10, max_bar=250000)


# return the cases by job title
class SalaryRange(restful.Resource):
    def get(self):
        # format
        return [salary_range_2017, salary_range_2018, salary_range_2019, salary_range_2020, salary_range_2021]


api.add_resource(SalaryRange, "/salary_range")

df = pd.read_csv("../../data/feature_importance.csv", index_col="name")
class FeatureImportance(restful.Resource):
    def get(self):
        return [df.to_dict()]
api.add_resource(FeatureImportance, "/feature_importance")

print(predictor.predict(["TEKSHAPERS, INC.", "", "Marketing Managers", "45411.0", "Y",
                       "Year", "Year", "Seattle", "WA", 1.0, 125171.0, 137400.0]))
class PredictCaseProb(restful.Resource):
    def get(self):
        args = parser.parse_args()
        data_preprocessing.cleaning(args)
        print(args)
        args['employer'] = args['employer'].replace("INC", "")
        args['employer'] = args['employer'].replace("LLC", "")
        return predictor.predict([data_preprocessing.cleaning(args['employer']), "", args['jobTitle'], "45411.0", "Y",
                       "Year", "Year", data_preprocessing.cleaning(args['city']), args['state'], 1.0, args['wage'], args['wage']]).tolist()
api.add_resource(PredictCaseProb, "/predict_case_prob")

# attr_list = {\
#     "CASE_NUMBER": None,
#     "CASE_STATUS": None,
#     "CASE_SUBMITTED": None,
#     "DECISION_DATE": None,
#     "EMPLOYER_NAME": None,
#     "EMPLOYER_BUSINESS_DBA": None,
#     "EMPLOYER_STATE": None,
#     "EMPLOYER_COUNTRY": None,
#     "SOC_NAME": None, #"SOC_TITLE"
#     "TOTAL_WORKER_POSITIONS": None,
#
# # WORKSITE_CITY_1,WORKSITE_COUNTY_1,WORKSITE_STATE_1,WORKSITE_POSTAL_CODE_1
#     "WORKPLACE_CITY": None,
#     "WORKPLACE_STATE": None,
#     "WORKPLACE_COUNTRY": None,
#     "WORKPLACE_POSTAL_CODE": None,
#
# #
#     "NAICS_CODE": None,
#     "PW_WAGE_LEVEL": None,
#     "PREVAILING_WAGE": None,
#     "WAGE_RATE_OF_PAY_FROM": None,
#     "WAGE_RATE_OF_PAY_TO": None,
#     "WAGE_UNIT_OF_PAY": None,
#
#     "H-1B_DEPENDENT": None,
#     "SUPPORT_H1B": None,
#     # "CASE_STATUS": None,
#     # "JOB_TITLE": None,
#     # "SOC_TITLE": None,
#     # "FULL_TIME_POSITION": None,
# }


# df_shape_17 = reader.read_raw_data("dataset/H-1B_Disclosure_Data_FY17.csv", attr_list = attr_list, write_csv = True)
# df_shape_18 = reader.read_raw_data("dataset/H-1B_Disclosure_Data_FY2018_EOY.csv", attr_list = attr_list, write_csv = False)
# df_shape_19 = reader.read_raw_data("dataset/H-1B_Disclosure_Data_FY2019.csv", attr_list = attr_list, write_csv = True)
# df_shape_20_Q1 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2020_Q1.csv", attr_list = attr_list, write_csv = False)
# df_shape_20_Q2 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2020_Q2.csv", attr_list = attr_list, write_csv = False)
# df_shape_20_Q3 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2020_Q3.csv", attr_list = attr_list, write_csv = False)
# df_shape_20_Q4 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2020_Q4.csv", attr_list = attr_list, write_csv = False)
# df_shape_21_Q1 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2021_Q1.csv", attr_list = attr_list, write_csv = False)
# df_shape_21_Q2 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2021_Q2.csv", attr_list = attr_list, write_csv = False)
# df_shape_21_Q3 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2021_Q3.csv", attr_list = attr_list, write_csv = False)
# df_shape_21_Q4 = reader.read_raw_data("dataset/LCA_Disclosure_Data_FY2021_Q4.csv", attr_list = attr_list, write_csv = False)
# possible social job titles/names
job_titles = []

if __name__ == '__main__':
    app.run(debug=True)
