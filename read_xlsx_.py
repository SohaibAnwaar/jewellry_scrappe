import pandas as pd

# Read Excel file
excel_file = pd.ExcelFile('ML_AttributesDefinition_NER.xlsx')

# Iterate over each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a pandas dataframe
    print(sheet_name)
    df = excel_file.parse(sheet_name)
    if sheet_name ==  'ATTRIBUTES':
        df = df.drop('DESCRIPTION', axis=1)
    # Prepare the CSV file name
    csv_file_name = sheet_name + '.csv'
    print(df)
    # Write the dataframe to a CSV file
    df.to_csv(f"/Users/sohaib/Documents/jewellry_scrappe/NewAttributes/{csv_file_name}", index=False)