import pandas as pd

#Load cleaned data
df = pd.read_csv('cleaned_data.csv')

#Group by 'Region' and calculate total sales
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

#Group by 'Product' and calculate average sales
product_avg = df.groupby('Product')['Sales'].mean().reset_index()

#Group by multiple columns
summary = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()

#Export to Excel
with pd.ExcelWriter('aggregated_report.xlsx', engine='openpyxl') as writer:
    region_sales.to_excel(writer, index=False, sheet_name='By Region')
    product_avg.to_excel(writer, index=False, sheet_name='By Product')
    summary.to_excel(writer, index=False, sheet_name='Region_Product')