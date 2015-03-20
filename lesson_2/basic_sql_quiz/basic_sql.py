import pandas
import pandasql

def select_first_50(filename):
    aadhaar_data = pandas.read_csv(filename)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax.

    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    q = """
    SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50;
    """

    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == "__main__":
    input_filename =  "aadhaar_data.csv"
    output_filename = "output.csv"
    aadhaar_solution = select_first_50(input_filename)
    aadhaar_solution.to_csv(output_filename)