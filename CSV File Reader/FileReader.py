import pandas as pd

#Read data from CSV
csv_data = pd.read_csv("data.csv")
print("CSV Data:")
print(csv_data)

#Write to Excel
csv_data.to_excel("data_output.xlsx", index=False)

#Read back from Excel
excel_data = pd.read_excel("data_output.xlsx")
print("\nExcel Data:")
print(excel_data)