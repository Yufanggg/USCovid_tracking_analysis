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
        # get the df info
        print(df.head())
        print(df.shape)
        print(df.columns)
        print(df.info())

        # extrat year, month and day out of the date
        # Convert the 'date' column to strings
        df['date'] = df['date'].astype(str)
        df['year'] = df['date'].str[:4]
        df['month'] = df['date'].str[4:6]
        df['day'] = df['date'].str[6:]

        # Save DataFrame to a CSV file
        df.to_csv('UScovid_tracking.csv', index=False)
        print("DataFrame saved to 'UScovid_tracking.csv'")

        # Create a new DataFrame marking values as 0 (for null) or 1 (for non-null)
        self.null_non_null_table = df.notnull().astype(int)
        print(df.info())

    #     # Change data type
    #     df = df.astype({'date':"int", 'states': "int", 'positive':"int", 'negative':"int", 'pending': "int",
    #    'hospitalizedCurrently': "int", 'hospitalizedCumulative': "int", 'inIcuCurrently': "int",
    #    'inIcuCumulative': "int", 'onVentilatorCurrently': "int", 'onVentilatorCumulative': "int",
    #    'dateChecked': "int", 'death': "int", 'hospitalized': "int", 'totalTestResults': "int",
    #    'lastModified': "int", 'recovered': "int", 'total': "int", 'posNeg': "int", 'deathIncrease': "int",
    #    'hospitalizedIncrease': "int", 'negativeIncrease': "int", 'positiveIncrease': "int",
    #    'totalTestResultsIncrease': "int"})

        # # Drop unwanted rows
        # self.df = df[df["states"] == 56]
        # Drop the unwanted column
        df.drop(columns=['hash'], inplace=True)
        self.df = df
        # Verify DataFrame content
        # print("DataFrame content before saving to SQL:")
        # print(self.df)
        print("STEP2: Done TRANSFORMING the data.")
        
    def load_data(self):
        '''
        Load the data into sqllite database
        '''
        try:
            sql_engine = create_engine('sqlite:///us_covid.db')
            # save data frame to SQL
            self.df.to_sql('UScovid_tracking', sql_engine, if_exists='replace')
            self.null_non_null_table.to_sql("UScovid_tracking_null_non_null", sql_engine, if_exists = "replace")
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
    # Create a SQL engine
    sql_engine = create_engine('sqlite:///us_covid.db')
    
    # Query to retrieve data from the 'UScovid_tracking' table
    query_UScovid_tracking = "SELECT * FROM UScovid_tracking"
    df_UScovid_tracking = pd.read_sql(query_UScovid_tracking, sql_engine)
    # Query to retrieve data from the 'UScovid_tracking_null_non_null' table
    query_null_non_null = "SELECT * FROM UScovid_tracking_null_non_null"
    df_null_non_null = pd.read_sql(query_null_non_null, sql_engine)
    
    # Display the data
    print("Data from 'UScovid_tracking' table:")
    print(df_UScovid_tracking)
    print("\nData from 'UScovid_tracking_null_non_null' table:")
    print(df_null_non_null)