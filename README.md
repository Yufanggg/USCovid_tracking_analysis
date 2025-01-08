# COVID-19 pandemic for the US Analysis
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/yufang-w-1295881b5/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&colorB=555)](https://github.com/Yufanggg) <img alt="GitHub" src="https://img.shields.io/github/license/bopith/UnicornCompanies?style=for-the-badge"> 



This repository contains the ETL (Extract, Transform and load) data into a SQL database SQL queries and the slide presentation for the analytical project on COVID-19 pandemic for the US Analysis

This project aims at exploring the answers to the following questions:
1. How have the positive and negative COVID-19 cases trended over time? Are there any noticeable spikes or drops in the number of positive or negative cases?
2. How have the numbers of currently hospitalized and ICU patients changed over time? What are the trends in cumulative hospitalizations and ICU admissions?
3. How has the number of patients currently on ventilators changed over time? What are the trends in cumulative ventilator usage?
4. How have the number of deaths and death increases trended over time? Are there any significant periods with higher death rates?
5. How have the total test results and test result increases trended over time? Are there any correlations between testing increases and positive case increases?
6. How do different states compare in terms of positive cases, hospitalizations, ICU admissions, and deaths?
Are there any states that consistently show higher or lower numbers across these metrics?
7. How have the number of pending cases changed over time? Are there any correlations between pending cases and other metrics like positive cases or hospitalizations?
8. How complete is the data for each metric? Are there any metrics with significant amounts of missing data?
How might missing data impact the analysis and conclusions?



## Data

The dataset used in this analysis contains records of daily data on the COVID-19 pandemic for the US and individual states obtained from [The COVID Tracking Project](https://covidtracking.com/). <br />

Information on the dataset include:
- `date` : *integer*, Date on which data was collected by The COVID Tracking Project.
- `death` : *integer* (*null* if no data is available), Deaths (confirmed and probable). Total fatalities with confirmed OR probable COVID-19 case diagnosis (per the expanded CSTE case definition of April 5th, 2020 approved by the CDC). In some states, these individuals must also have COVID-19 listed on the death certificate to count as a COVID-19 death. When states post multiple numbers for fatalities, the metric includes only deaths with COVID-19 listed on the death certificate, unless deaths among cases is a more reliable metric in the state.
- `deathIncrease` : *integer* (*null* if no data is available), Daily increase in death, calculated from the previous day’s value.
- `hospitalized` : *integer* (*null* if no data is available), Old label for `hospitalizedCumulative`.
- `hospitalizedCumulative` : *integer* (*null* if no data is available), Cumulative hospitalized/Ever hospitalized, Total number of individuals who have ever been hospitalized with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients hospitalized with confirmed or suspected COVID-19 cases.
 - `hospitalizedCurrently` : *integer* (*null* if no data is available), Currently hospitalized/Now hospitalized. Individuals who are currently hospitalized with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients hospitalized with confirmed or suspected COVID-19 cases.
- `hospitalizedIncrease`: *integer* (*null* if no data is available), New total hospitalizations. Daily increase in hospitalizedCumulative, calculated from the previous day’s value.
- `inIcuCumulative`:  *integer* (*null* if no data is available), Cumulative in ICU/Ever in ICU. Total number of individuals who have ever been hospitalized in the Intensive Care Unit with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients in the ICU with confirmed or suspected COVID-19 cases.
- `inIcuCurrently` :  *integer* (*null* if no data is available), Currently in ICU/Now in ICU. Individuals who are currently hospitalized in the Intensive Care Unit with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients in the ICU with confirmed or suspected COVID-19 cases.
- `lastModified` : *string*, Deprecated. Old label for lastUpdateET.
- `negative` : *integer* (*null* if no data is available), Negative PCR tests (people). Total number of unique people with a completed PCR test that returns negative. For states / territories that do not report this number directly, we compute it using one of several methods, depending on which data points the state provides. Due to complex reporting procedures, this number might be mixing units and therefore, at best, it should only be considered an estimate of the number of people with a completed PCR test that return negative.
- `negativeIncrease` : *integer* (*null* if no data is available), Increase in negative computed by subtracting the value of negative for the previous day from the value for negative from the current day.
- `onVentilatorCumulative` : *integer* (*null* if no data is available), Cumulative on ventilator/Ever on ventilator. Total number of individuals who have ever been hospitalized under advanced ventilation with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients on ventilation with confirmed or suspected COVID-19 cases.
- `onVentilatorCurrently` : *integer* (*null* if no data is available), Currently on ventilator/Now on ventilator. Individuals who are currently hospitalized under advanced ventilation with COVID-19. Definitions vary by state / territory, and it is not always clear whether pediatric patients are included in this metric. Where possible, we report patients on ventilation with confirmed or suspected COVID-19 cases.
- `pending` : *integer* (*null* if no data is available), Pending. Total number of viral tests that have not been completed as reported by the state or territory.
- `posNeg` : *integer* (*null* if no data is available), Deprecated. Computed by adding positive and negative values.
- `positive` : *integer* (*null* if no data is available), Cases (confirmed plus probable). Total number of confirmed plus probable cases of COVID-19 reported by the state or territory, ideally per the August 5, 2020 CSTE case definition. Some states are following the older April 5th, 2020 CSTE case definition or using their own custom definitions. Not all states and territories report probable cases. If a state is not reporting probable cases, this field will just represent confirmed cases.
- `positiveIncrease` : *integer* (*null* if no data is available), New cases. The daily increase in API field positive, which measures Cases (confirmed plus probable) calculated based on the previous day’s value.
- `recovered` :  *integer* (*null* if no data is available), Recovered. Total number of people that are identified as recovered from COVID-19. States provide very disparate definitions on what constitutes a “recovered” COVID-19 case. Types of “recovered” cases include those who are discharged from hospitals, released from isolation after meeting CDC guidance on symptoms cessation, or those who have not been identified as fatalities after a number of days (30 or more) post disease onset. Specifics vary for each state or territory.
- `states` : *integer*, States. Only available in national records. The number of states and territories included in the US dataset for this day.
- `total` :  *integer* (*null* if no data is available), Deprecated. Computed by adding positive, negative, and pending values.
- `totalTestResults` :  *integer* (*null* if no data is available), Total test results. At the national level, this metric is a summary statistic which, because of the variation in test reporting methods, is at best an estimate of US viral (PCR) testing. Some states/territories report tests in units of test encounters, some report tests in units of specimens, and some report tests in units of unique people. Moreover, some jurisdictions include antigen tests in their total test counts without reporting a separate total of viral (PCR) tests. Therefore, this value is an aggregate calculation of heterogeneous figures. Please consult each state or territory’s individual data page to see whether that jurisdiction lumps antigen and PCR tests together and to see what units that jurisdiction uses for test reporting. 

In most states, the totalTestResults field is currently computed by adding positive and negative values because, historically, some states do not report totals, and to work around different reporting cadences for cases and tests. In Colorado, Delaware, the District of Columbia, Florida, Hawaii, Minnesota, Nevada, New York, North Dakota, Pennsylvania, Rhode Island, Virginia, Washington, and Wisconsin, where reliable testing encounters figures are available with a complete time series, we directly report those figures in this field. In Alaska, America Samoa, Arizona, Arkansas, California, Connecticut, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, Missouri, Montana, Nebraska, New Hampshire, New Mexico, North Carolina, Ohio, Oregon, South Dakota, Tennessee, Texas, Utah, Vermont, West Virginia, and Wyoming, where reliable specimens figures are available with a complete time series, we directly report those figures in this field. In Alabama and Idaho where reliable unique people figures are available with a complete time series, we directly report those figures in this field. We are in the process of switching all states over to use directly reported total figures, using a policy of preferring testing encounters, specimens, and people, in that order.

- `totalTestResultsIncrease` : *integer* (*null* if no data is available), New tests. Daily increase in totalTestResults, calculated from the previous day’s value. This calculation includes all the caveats associated with Total tests/totalTestResults, and we recommend against using it at the state/territory level.





## SQL Queries

- `data_cleaning.sql`: a query for data cleaning
- `data_exploration.sql`: a query for data exploration
- `query_data_visualization.sql`: a query for data visualization in PowerBI


## Analytical Results

Brief findings of this project are:
1. Zapier has the biggest return on investment.
2. It usually takes about 6 years to become a unicorn.
3. Fintech industry has the most unicorns.
4. The United States has the most unicorns.
5. Accel has funded the most unicorns.

Please check `uc_covid_results.pdf` for more details and meaningful discussion on query outputs and analytical results.

Tableau Dashboard:
![Dashboard](/img/dashboard.png?raw=true)


## Acknowledgments
