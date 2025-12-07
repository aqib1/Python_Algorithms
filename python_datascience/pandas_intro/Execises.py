import pandas as pd

def contains(job_title: str):
    if job_title.__contains__('Chief'):
        return True
    else:
        return False

if __name__ == '__main__':
    salaries = pd.read_csv('Salaries.csv')
    print(salaries)

    print('*' * 50)
    ### Check the head of the DataFrame
    print(salaries.head())

    print('*' * 50)
    ### Get info
    print(salaries.info())

    print('*' * 50)
    ### Average Base pay
    print(salaries['BasePay'].mean())

    print('*' * 50)
    ### Maximum OvertimePay
    print(salaries['OvertimePay'].max())

    print('*' * 50)
    ### get job title
    print(salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

    print('*' * 50)
    ### how much JOSEPH makes including benefits.
    print(salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

    print('*' * 50)
    ### Name of highest paid person including benefits.
    print(salaries[
              salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].max()
          ]['EmployeeName'])

    print('*' * 50)
    ### Name of highest paid person including benefits.
    print(salaries[
              salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()
              ]['EmployeeName'])


    print('*' * 50)
    ### Average (mean) BasePay of all employees per year?
    print(salaries.groupby('Year')['BasePay'].mean())

    print('*' * 50)
    ### Unique job titles
    print(salaries['JobTitle'].unique())
    print(salaries['JobTitle'].nunique())

    print('*' * 50)
    ### Top 5 most common jobs
    print(salaries['JobTitle'].value_counts().head(n=5))

    print('*' * 50)
    ### How many Job Titles were represented by only one person in 2013
    salaries_value_counts = salaries[salaries['Year'] == 2013]['JobTitle'].value_counts()
    print(salaries_value_counts[salaries_value_counts == 1])
    print(sum(salaries_value_counts[salaries_value_counts == 1]))