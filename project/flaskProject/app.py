from flask import Flask
import flask_restful as restful
import data_reader as util

app = Flask(__name__)
api = restful.Api(app)
@app.route("/download/<filepath>", methods=['GET'])
def download_file(filepath):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file(filepath)


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
df_reader_2017 = util.H1bDataReader("../../data/h1b_data_2017.csv", attr_list = attr_list)
df_reader_2018 = util.H1bDataReader("../../data/h1b_data_2018.csv", attr_list = attr_list)
df_reader_2019 = util.H1bDataReader("../../data/h1b_data_2019.csv", attr_list = attr_list)
df_reader_2020 = util.H1bDataReader("../../data/h1b_data_2020.csv", attr_list = attr_list)
df_reader_2021 = util.H1bDataReader("../../data/h1b_data_2021.csv", attr_list = attr_list)
df_reader_2017.state_preprocess()
df_reader_2018.state_preprocess()
df_reader_2019.state_preprocess()
df_reader_2020.state_preprocess()
df_reader_2021.state_preprocess()
df_reader_2017.salary_preprocess()
df_reader_2018.salary_preprocess()
df_reader_2019.salary_preprocess()
df_reader_2020.salary_preprocess()
df_reader_2021.salary_preprocess()
df_reader_2017.casestate_preprocess()
df_reader_2018.casestate_preprocess()
df_reader_2019.casestate_preprocess()
df_reader_2020.casestate_preprocess()
df_reader_2021.casestate_preprocess()

#case_status
case_status_17 = df_reader_2017.attr_operator("CASE_STATUS")
case_status_18 = df_reader_2018.attr_operator("CASE_STATUS")
case_status_19 = df_reader_2019.attr_operator("CASE_STATUS")
case_status_20 = df_reader_2020.attr_operator("CASE_STATUS")
case_status_21 = df_reader_2021.attr_operator("CASE_STATUS")

# worksite_state
worksite_state = df_reader_2017.attr_operator("WORKSITE_STATE")

#number of visa applications by employer_name
cases_by_employer_17 = df_reader_2017.attr_operator("EMPLOYER_NAME", head = 10)
cases_by_employer_18 = df_reader_2018.attr_operator("EMPLOYER_NAME", head = 10)
cases_by_employer_19 = df_reader_2019.attr_operator("EMPLOYER_NAME", head = 10)
cases_by_employer_20 = df_reader_2020.attr_operator("EMPLOYER_NAME", head = 10)
cases_by_employer_21 = df_reader_2021.attr_operator("EMPLOYER_NAME", head = 10)

#number of visa applications by soc_name
cases_by_job_title_17 = df_reader_2017.attr_operator("SOC_NAME", head = 10)
cases_by_job_title_18 = df_reader_2018.attr_operator("SOC_NAME", head = 10)
cases_by_job_title_19 = df_reader_2019.attr_operator("SOC_NAME", head = 10)
cases_by_job_title_20 = df_reader_2020.attr_operator("SOC_NAME", head = 10)
cases_by_job_title_21 = df_reader_2021.attr_operator("SOC_NAME", head = 10)



df_shape_17 = df_reader_2017.get_df_shape()[0]
df_shape_18 = df_reader_2018.get_df_shape()[0]
df_shape_19 = df_reader_2019.get_df_shape()[0]
df_shape_20 = df_reader_2020.get_df_shape()[0]
df_shape_21 = df_reader_2021.get_df_shape()[0]





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

#all possible job titles
class JobTitles(restful.Resource):
    def get(self):
        return job_titles
api.add_resource(JobTitles, "/job_titles")

#return the CertifiedRateByState when user searching by job title
class JobCertifiedRateByState(restful.Resource):
    def get(self, job_title):
        # format
        return {
            "state1":{
                "test": job_title
            },
            "state2":{
                "test2": job_title
            }
        }
api.add_resource(JobCertifiedRateByState, "/job_certified_rate_by_state/<string:job_title>")

#return the case status
class CASE_STATUS(restful.Resource):
    def get(self):
        # format
        return [case_status_17, case_status_18, case_status_19, case_status_20, case_status_21]
api.add_resource(CASE_STATUS, "/case_status")

#return the case status
class WORKSITE_STATE(restful.Resource):
    def get(self):
        # format
        return worksite_state
api.add_resource(WORKSITE_STATE, "/worksite_state")

#return the case status
class USTopo(restful.Resource):
    def get(self):
        # format
        return [case_status_17, case_status_18, case_status_19, case_status_20, case_status_21]
api.add_resource(USTopo, "/us_topo")

#return the cases by employer
class CasesByEmployer(restful.Resource):
    def get(self):
        # format
        return [cases_by_employer_17, cases_by_employer_18, cases_by_employer_19, cases_by_employer_20, cases_by_employer_21]
api.add_resource(CasesByEmployer, "/cases_by_employer")

#return the cases by job title
class CasesByJobTitle(restful.Resource):
    def get(self):
        # format
        return [cases_by_job_title_17, cases_by_job_title_18, cases_by_job_title_19, cases_by_job_title_20, cases_by_job_title_21]
api.add_resource(CasesByJobTitle, "/cases_by_job_title")


salary_range_2017 = df_reader_2017.salary_range(split=10, max_bar=250000)
salary_range_2018 = df_reader_2018.salary_range(split=10, max_bar=250000)
salary_range_2019 = df_reader_2019.salary_range(split=10, max_bar=250000)
salary_range_2020 = df_reader_2020.salary_range(split=10, max_bar=250000)
salary_range_2021 = df_reader_2021.salary_range(split=10, max_bar=250000)
#return the cases by job title
class SalaryRange(restful.Resource):
    def get(self):
        # format
        return [salary_range_2017, salary_range_2018, salary_range_2019, salary_range_2020, salary_range_2021]
api.add_resource(SalaryRange, "/salary_range")
class FeatureImportance(restful.Resource):
    def get(self):
        df = pd.read_csv("../../data/feature_importance.csv", index_col="name")
        return [df.to_dict()]
api.add_resource(FeatureImportance, "feature_importance")

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
#possible social job titles/names
job_titles = []

if __name__ == '__main__':
    app.run(debug=True)