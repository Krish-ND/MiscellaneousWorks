import pandas as pd

#Read raw data
df = pd.read_csv('sales_data.csv')

#Perform summary (example: total sales by region)
summary = df.groupby('Region')['Sales'].sum().reset_index()

#Write to Excel
with pd.ExcelWriter('sales_report.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Raw Data')
    summary.to_excel(writer, index=False, sheet_name='Summary')