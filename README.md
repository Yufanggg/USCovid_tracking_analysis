# COVID-19 pandemic for the US Analysis
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/yufang-w-1295881b5/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&colorB=555)](https://github.com/Yufanggg) <img alt="GitHub" src=" https://img.shields.io/github/license/Yufanggg/USCovid_tracking_analysis?style=for-the-badge">

## Overview
This repository contains the ETL (Extract, Transform and load) data into a SQL database SQL queries and the slide presentation for the analytical project on COVID-19 pandemic for the US Analysis

This project aims at exploring the answers to the following questions:
1. How have the positive and negative COVID-19 cases trended over time? Are there any noticeable spikes or drops in the number of positive or negative cases?
2. How have the numbers of currently hospitalized and ICU patients changed over time? What are the trends in cumulative hospitalizations and ICU admissions?
3. How complete is the data for each metric? Are there any metrics with significant amounts of missing data?

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Data](#Data)
- [Project Structure](#project-structure)
- [Results](#Results)

## Requirments
To run this Project, you will need the following:
- Python (> 3.6)
- Pandas (pip install pandas)
- Requests (pip install requests)
- SQLAlchemy (pip install sqlalchemy)

## Installation

1. Clone the repository to local machine:
   ```
   git clone https://github.com/Yufanggg/USCovid_tracking_analysis.git    
   ```

2. Navigate to the project directory:
   ```
   cd USCovid_tracking_analysis
   ```

3. Intsall the required Python packages:
   ```
   pip install -r requires.txt
   ```



## Data

The dataset used in this analysis contains records of daily data on the COVID-19 pandemic for the US and individual states obtained from [The COVID Tracking Project](https://covidtracking.com/). <br />

Information on the dataset include:
- `date` : *integer*, Date on which data was collected by The COVID Tracking Project.
- `death` : *integer* (*null* if no data is available), Deaths (confirmed and probable). 
 - `hospitalizedCurrently` : *integer* (*null* if no data is available), Currently hospitalized/Now hospitalized. 
- `inIcuCurrently` :  *integer* (*null* if no data is available), Currently in ICU/Now in ICU. 
- `negative` : *integer* (*null* if no data is available), Negative PCR tests (people). 
- `positive` : *integer* (*null* if no data is available), Cases (confirmed plus probable). 

## Project Struture

### ETL tools 
To load data from the web, and save it in a database `us_covid.db` with two separate tables: `UScovid_tracking` and `UScovid_tracking_null_non_null`. The first one is the original dataset. The second one is about the missing data cases. This can be call with the following command: 

```
python ETL.py
```

### PowerBI Dashboard:
To build up a [PowerBI Dashboard](./covid_tracking.pbix) to have a general idea about the data, see a screeshot as following: 
![alt text](./Images/covid_tracking.jpg)

### PowerBI Dashboard:
To build up a [PowerBI Dashboard](./covid_tracking.pbix) to have a general idea about the data, see a screeshot as following: 
![alt text](./Images/covid_tracking.jpg)

### SQL Queries

- `query_data_visualization.sql`: a query for data visualization in PowerBI


## Results

Brief findings of this project are:
1. Zapier has the biggest return on investment.
2. It usually takes about 6 years to become a unicorn.
3. Fintech industry has the most unicorns.
4. The United States has the most unicorns.
5. Accel has funded the most unicorns.

Please check `uc_covid_results.pdf` for more details and meaningful discussion on query outputs and analytical results.




## Acknowledgments
