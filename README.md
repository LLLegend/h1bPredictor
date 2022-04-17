# H1-B Visa Trends Visualization and Predictor
## Georgia Tech CSE6242 Sp '22 RSZ
## Members
- Alex
- Chuanqi
- Qinrui
- Tianshu
- Tianyu

README.txt - a concise, short README.txt file, corresponding to the "user guide".

This file should contain:
## DESCRIPTION
    
This package contains all the necessary tools to process, H1-B application data from US Department of Labor statistics, generate visualizations based on the statistics and their trends, and run a predictor on application certification likelihood based on user-determined parameters. 

The datasets were directly downloaded from the US Department of Labor's webpage on Performance Data. 
We have preprocessed the data, unifying the attribute names for all the years' datasets and removing extraneous attributes. 

The Flask-Vue app consists of a home page with several links to views of 
dynamic visualizations of the statistics drawn from the data sets. 
All visualizations are dynamic charts created with D3.js.  

The predictor is a gradient-boosted decision tree using the LightGBM framework. 

## INSTALLATION 

Download the .zip package. 

What dependencies do we have?

 - Download NPM?

 - Download D3?

 - Download data?

The preprocessed datasets can be accessed in cloud storage by the links provided below: 

https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2017.csv
https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2018.csv
https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2019.csv
https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2020.csv
https://abuddenbaum3.blob.core.windows.net/h1b/h1b_data_2021.csv



## EXECUTION - How to run a demo on your code

Where do I open the terminal?

What commands do I enter? 

What URL should I enter in my browser? 


## DEMO VIDEO - [Optional, but recommended] 

Include the URL of a 1-minute *unlisted* YouTube video in this txt file. The video would show how to install and execute your system/tool/approach (e.g, from typing the first command to compile, to system launching, and running some examples).

Feel free to speed up the video if needed (e.g., remove less relevant video
segments). This video is optional (i.e., submitting a video does not increase scores; not submitting one does not decrease scores). However, we
recommend teams to try and create such a video, because making the video
helps teams better think through what they may want to write in the
README.txt, and generally how they want to "sell" their work.