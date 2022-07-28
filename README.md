# H1-B Visa Trends Visualization and Predictor
## Members
- Alex
- Chuanqi
- Qinrui
- Tianshu
- Tianyu

## Description

This package contains all the necessary tools to process, H1-B application data from US Department of Labor statistics, generate visualizations based on the statistics and their trends, and run a predictor on application certification likelihood based on user-determined parameters. 

The datasets were directly downloaded from the US Department of Labor's webpage on Performance Data. 
We have preprocessed the data, unifying the attribute names for all the years' datasets and removing extraneous attributes. 

The Flask-Vue app consists of a home page with several links to views of 
dynamic visualizations of the statistics drawn from the data sets. 
All visualizations are dynamic charts created with D3.js.  

The predictor is a gradient-boosted decision tree using the LightGBM framework. 

## Installation 

Download the .zip package. 

Or `git clone https://github.com/budd713/datadreamteam.git` after we open our project as public.

##### Dataset

<!-- - The dataset is with the project in PROJECT_ROOT/data. -->

- The preprocessed datasets can be accessed in cloud storage by the links provided below (there should be 5). Please download them and place them in PROJECT_ROOT/data.:

  https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2017_new.csv
  https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2018_new.csv
  https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2019_new.csv
  https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2020_new.csv
  https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2021_new.csv


##### Frontend

 - Be sure to have NodeJs v14.17.x installed (or npm v6.14.x).
 - Run `npm install` in the root directory of front-end PROJECT_ROOT/project/frontend.

##### Backend

Be sure to have python v3.8.x with flask-restful v0.3.9 and pandas installed.

- if not, download python3 from its official website 
- then run `pip install -v flask==2.0.2` 
- `pip install -v flask-restful==0.3.9`
- `pip install -v pandas==2.3`
- `pip install -v numpy==1.21.2`
- `pip install -v lightgbm==3.2.1`



## Execution

Run `python app.py` in the root directory of back-end PROJECT_ROOT/flaskProject to launch the back-end service and wait for a few minutes (it may depend on your machine) to read and preprocess the data.

Run `npm run serve` in the root directory of front-end PROJECT_ROOT/frontend to launch the frontend project.

Enter `localhost:8080` in your browser to explore and enjoy our project!
