#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install --upgrade google-cloud-bigquery


# In[4]:


pip install google-cloud-bigquery


# In[ ]:





# In[5]:


pip install google-cloud


# In[6]:


pip install google-cloud-vision


# In[7]:


pip install --upgrade google-cloud-storage


# In[ ]:





# In[ ]:





# In[8]:


import os
import pandas as pd
from google.cloud import bigquery


# In[9]:


# Set path to your downloaded JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/DELL/Downloads/ethereal-fort-464005-e3-64bf1a610db8.json"

# Create BigQuery client
client = bigquery.Client()

# Test
print("BigQuery client created for project:", client.project)


# In[10]:


from datetime import datetime


# In[13]:


# Get the current date
today = datetime.today()

# Calculate start of the previous week (Monday)
start_date = today - timedelta(days=today.weekday() + 7)

# Calculate end of the previous week (Sunday)
end_date = start_date + timedelta(days=6)

# Calculate the week number for the previous week
week_num = int(end_date.strftime('%U')) 


# In[12]:


from datetime import timedelta


# In[ ]:


week_num


# In[ ]:


today


# In[ ]:


start_date


# In[ ]:


end_date


# In[14]:


# Format dates to more readable form for folder creation
try:
    # Format start_date and end_date to strings for formatting
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Parse start_date and end_date into the desired format
    start_date_components = start_date_str.split('-')
    start_date_formatted = f"{int(start_date_components[1]):g}-{int(start_date_components[2]):g}-{start_date_components[0][-2:]}"

    end_date_components = end_date_str.split('-')
    end_date_formatted = f"{int(end_date_components[1]):g}-{int(end_date_components[2]):g}-{end_date_components[0][-2:]}"

    folder_name = f"{week_num} {start_date_formatted} to {end_date_formatted}"

    # Define path for main report folder and ensure it's created
    main_folder_path = os.path.join(r'computer\file\path', folder_name)
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
    print(f"Folder created at: {main_folder_path}")

except ValueError as ve:
    print(f"Error processing date formats: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# In[15]:


# Define SQL query using parameters for flexibility and security
query = """
WITH transactions AS (
    SELECT 
        DATE(timestamp) as purchase_date, 
        SUM(amount_usd) as total_purchases
    FROM 
        `ethereal-fort-464005-e3.finance_data.transactions`
    GROUP BY purchase_date
),
expenses AS (
    SELECT 
        DATE(timestamp) as expense_date, 
        SUM(expenses) as total_expenses
    FROM 
        `ethereal-fort-464005-e3.finance_data.expenses`
    GROUP BY expense_date
)
SELECT 
    day, 
    FORMAT_DATE('%a', day) as day_of_the_week, 
    t.total_purchases, 
    e.total_expenses,
    (t.total_purchases - e.total_expenses) AS revenue
FROM 
    UNNEST(GENERATE_DATE_ARRAY('2024-06-01', '2024-06-03')) AS day
LEFT JOIN transactions t ON t.purchase_date = day
LEFT JOIN expenses e ON e.expense_date = day
ORDER BY day

"""


# In[16]:


# Configure query parameters to safeguard against SQL injection and provide flexibility
job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ScalarQueryParameter("start", "STRING", start_date_str),
        bigquery.ScalarQueryParameter("end", "STRING", end_date_str)
    ]
)

try:
    # Execute the query and load results into a pandas DataFrame
    query_job = client.query(query, job_config=job_config)
    df = query_job.to_dataframe()

    # Function to calculate net revenue from purchases and expenses
    def calculate_revenue(row):
        total_purchases = row['total_purchases']
        total_expenses = row['total_expenses']
        if total_purchases is None or total_expenses is None:
            return None
        return total_purchases - total_expenses

    # Apply the custom function to create a new column
    df['revenue'] = df.apply(calculate_revenue, axis=1)

    print("Query results:")
    print(df)

    # Setup paths and export results to CSV for further analysis and reporting
    csv_folder_path = os.path.join(main_folder_path, 'CSV')
    if not os.path.exists(csv_folder_path):
        os.makedirs(csv_folder_path)

    csv_file_name = f'Report Tables {start_date_formatted} to {end_date_formatted}.csv'
    csv_file_path = os.path.join(csv_folder_path, csv_file_name)
    df.to_csv(csv_file_path, index=False)

    print(f"CSV file: {csv_file_name} exported successfully to: {csv_file_path}")
except Exception as e:
    print("An error occurred during query execution:", e)


# In[ ]:


pip install db-dtypes


# In[ ]:




