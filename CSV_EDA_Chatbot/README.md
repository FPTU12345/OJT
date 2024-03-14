# Chatbot for analysing data on a specific CSV file
In this app, you can write a query to ask the chatbot what to draw and what steps to process the data.

## EDA
For Data Visualization for EDA, here are the available plots:
|Type|Test Image|
|--|--|
|Box plot|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo2.PNG)|
|Count plot|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo1.PNG)|
|Scatter plot|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo3.PNG)|
|Line plot|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo4.PNG)

In addition, here are some NLP visualizations are available:
|Type|Test Image|
|----|----------|
|Word cloud|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo8.PNG)|
|Top k word used the most|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo7.PNG)|
|Word Length Analysis|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo9.PNG)|

## Processing
Here are some popular methods to process the data are available:
* Drop missing value
* Impute missing value (with mean, mode or median)
* Drop columns
* Drop duplicates
* Impute outlier (with mean or median)
* Floor and cap outlier
* Change data type

|Input|Output|
|------|------|
|I want to drop the column called country.  As for the weight column, I want to cap and floor with percentile from 0.1 to 0.9. Impute the height column with mean  and change data type of column height into interger|![Image Link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo5.PNG)|
|Impute outlier on weight with mean and height with median and then drop duplicate first then missing value|![Image link](https://github.com/FPTU12345/OJT/blob/main/CSV_EDA_Chatbot/img/demo6.PNG)|
