import pandas
import pandasql

def complex_sql(filename):
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # PROBLEM: Write a query that will select from the aadhaar_data table how many men and how
    # many women over the age of 50 have had aadhaar generated for them in each district

    q = '''
    SELECT gender, district, SUM(aadhaar_generated)
    FROM aadhaar_data
    WHERE age>50
    GROUP BY gender, district;
    '''
    # We're interested in gender, district and aadhaar_generated and as such, SELECT THESE COLUMNS
    #   - The SUM(aadhaar_generated) will be calculated from the funnel from gender down to districts
    # FROM aadhaar_data
    # WHERE age > 50 - this is technically the only condition that we're interested in
    # GROUP BY - gender first, the first column will be gender and the data will be separated
    #          - district second, the data will further be grouped by district

    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == "__main__":
    input_filename = "aadhaar_data.csv"
    output_filename = "output.csv"
    pandas_df = complex_sql(input_filename)
    pandas_df.to_csv(output_filename)
