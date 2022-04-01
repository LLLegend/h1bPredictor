from flask import Flask
import flask_restful as restful
import data_reader as util

app = Flask(__name__)
api = restful.Api(app)
attr_list = {\
        "CASE_NUMBER": None,
        "CASE_STATUS": None,
        "SOC_NAME": None,
        "FULL_TIME_POSITION": None,
        "WORKSITE_STATE": None
    }
df_reader = util.H1bDataReader("../../data/h1b_data_2019.csv", attr_list = attr_list)
df_reader.state_preprocess()
case_status = df_reader.attr_operator("CASE_STATUS")
worksite_state = df_reader.attr_operator("WORKSITE_STATE")

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'GUNDAM'}

api.add_resource(HelloWorld, '/')

class Trends(restful.Resource):
    def get(self):
        # put application's code here
        return {
            # "2017": df_shape_17[0],
            # "2018": df_shape_18[0],
            # "2019": df_shape_19[0],
            # "2020": df_shape_20_Q1[0] + df_shape_20_Q2[0] + df_shape_20_Q3[0] + df_shape_20_Q4[0],
            # "2021": df_shape_21_Q1[0] + df_shape_21_Q2[0] + df_shape_21_Q3[0] + df_shape_21_Q4[0],
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
        return case_status
api.add_resource(CASE_STATUS, "/case_status")

#return the case status
class WORKSITE_STATE(restful.Resource):
    def get(self):
        # format
        return worksite_state
api.add_resource(WORKSITE_STATE, "/worksite_state")
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