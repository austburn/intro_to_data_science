import pandas as pd
import pandasql

def num_rainy_days(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained).  The dataframe will be titled 'weather_data'. You'll
    need to provide the SQL query.  You might find SQL's count function
    useful for this exercise.  You can read more about it here:

    https://dev.mysql.com/doc/refman/5.1/en/counting-rows.html

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.
    '''
    weather_data = pd.read_csv(filename)

    # SELECT the max maxtempi and group it by the fog value (0 or 1)
    q = """
    SELECT count(rain) FROM weather_data WHERE cast(rain as integer) = 1;
    """

    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days



if __name__ == "__main__":
    input_filename = "weather_underground.csv"
    output_filename = "output.csv"
    student_df = num_rainy_days(input_filename)
    student_df.to_csv(output_filename)