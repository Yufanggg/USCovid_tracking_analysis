import ETL

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