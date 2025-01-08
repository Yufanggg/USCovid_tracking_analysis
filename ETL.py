import pandas as pd
import requests
from sqlalchemy import create_engine


class ETL:
    def __init__(self, url):
        self.url = url
        self.dataTypeList = False

    def extract_data(self): 
        '''
        Download the data from an api
        Return: json data
        '''
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            if isinstance(data, list):
                self.dat = data  # Directly assign the list to self.dat
                self.dataTypeList = True
            else:
                self.dat = data.get("data")  # Handle dictionary case
            print("STEP 1: Done EXTRACTION data from the api.")    
        except Exception as e:
            print("Data extract error: " + str(e))

    def transform_data(self):
        '''
        Clean and transform the data to a specific format
        Return: cleaned dataset
        '''
        df = pd.DataFrame(self.dat)
        print(df.head())
        print(df.shape)
        # print(df.columns)
        print(df.info())
        # Remove rows with NA values
        df = df.dropna()
        # Change data type
        df = df.astype({"date":"int", "positive": "int", "negative": "int", 
                        "negativeIncrease": "int", "positiveIncrease": "int",                         
                        "totalTestResults":"int", "totalTestResultsIncrease": "int"})
        # Drop unwanted rows
        self.df = df[df["states"] == 56]
        print("STEP2: Done TRANSFORMING the data.")
        
    def load_data(self):
        '''
        Load the data into sqllite database
        '''
        try:
            sql_engine = create_engine('sqlite:///us_covid.db')
            self.df.to_sql('etl_project', sql_engine, if_exists='replace')
            print("STEP 3: Done LOADING data into database. \n...")
        except Exception as e:
            print("Data load error: " + str(e))

def main():

    # ETL
    url = "https://api.covidtracking.com/v1/us/daily.json"
    etl_proc = ETL (url = url)
    etl_proc.extract_data()
    etl_proc.transform_data()
    etl_proc.load_data()


if __name__ == "__main__":
    main()