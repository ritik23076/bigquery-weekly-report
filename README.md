# 🗂️ bigquery-python-weekly-report

> **Automating Weekly Financial Reports with BigQuery & Python**

A project that automates the generation of a weekly executive report using Google BigQuery, Python, and task automation tools. This report provides a snapshot of a company’s financial health by summarizing purchase and expense data from a database and exporting the results to a CSV file.

---

## 📌 Project Objective

This project was originally created to **save time** by automating a **weekly executive financial report**. It has since been enhanced to:

- Automatically update date ranges and week numbers
- Fetch data directly from BigQuery
- Perform revenue calculations
- Export results as a structured CSV file
- Run automatically on a set schedule

---

## 🧰 Tools & Technologies

| Tool                | Purpose                                  |
|---------------------|-------------------------------------------|
| **Python**          | Main programming language                 |
| **Google BigQuery** | Cloud database for querying large datasets|
| **pandas**          | Data manipulation and export to CSV       |
| **Anaconda**        | Python environment & package management   |
| **VS Code**         | Development environment                   |
| **GitHub**          | Version control and collaboration         |
| **Task Scheduler / Cron** | Running scripts automatically        |

---

## 🛠️ Automation Steps

### ✅ 1. Updated Python Script
The core script is named `weekly_report_automatic.py`.

Key features:
- Authenticates with BigQuery using a service account
- Uses parameterized SQL to query transaction and expense data
- Calculates daily revenue = `total_purchases - total_expenses`
- Stores results in a Pandas DataFrame
- Exports results to a dated CSV file

> Note: Data used is fictional and simplified for educational purposes.

---

### ✅ 2. Batch/Job File Creation (for Scheduling)
A shell script or batch file (`run_report.sh` or `.bat`) is used to:
- Activate the Anaconda environment
- Run the script with proper paths

This allows the report to run from **cron (macOS/Linux)** or **Task Scheduler (Windows)** without opening the terminal manually.

---

######  Aim of the project

To analyze daily revenue by combining purchase (transactions) and spending (expenses) data, using BigQuery for fast querying and Python + Pandas for reporting.

🧠 What This Project is Achieving
This project:

Connects to BigQuery from Python securely

Executes SQL queries that summarize business activity over time

Calculates daily revenue by subtracting expenses from purchases

Exports data to CSV reports that can be shared, visualized, or fed into dashboards

🧪 Example Output:
Date	Day	Purchases	Expenses	Revenue
2024-06-01	Sat	200	50	150
2024-06-02	Sun	300	60	240

📦 Use Cases (Real-World Applications)
This project structure is commonly used for:

1. Financial Reporting
Track daily/weekly/monthly revenue

Spot profit drops or overspending

2. Business Intelligence
Feed this data into dashboards (e.g., Power BI, Tableau, Looker)

Compare trends, identify growth days vs slow days

3. Automation & Scheduled Reports
Schedule the Python script to run daily (e.g., via cron jobs or Cloud Functions)

Automatically email reports to stakeholders

4. Forecasting
Use the data to train ML models for forecasting expenses or revenue

5. Anomaly Detection
Detect days with unusually high expenses or revenue

💡 Skills & Tech Demonstrated
Area	Skills
Cloud	Google BigQuery, IAM, GCP authentication
Programming	Python, pandas, SQL
Data Engineering	Loading, transforming, querying datasets
Analytics	Revenue metrics, time-based summaries
Automation	Exporting reports to CSV for reuse or visualization

🧱 Summary
This project showcases how cloud analytics pipelines work — from raw data (transactions, expenses) to processed, actionable insights (daily revenue reports).
It’s a great resume-ready project showing real-world business use of SQL, Python, BigQuery, and reporting workflows.

#### ❓What If You Don’t Use This Automation (BigQuery + Python)?
🔴 Drawbacks of NOT Automating:
Aspect	Manual Way	Drawback
📊 Data Processing	Manually write queries, download data from UI	Time-consuming, error-prone
🧮 Revenue Calculation	Manually compute revenue in Excel	Risk of formula mistakes, no version control
📁 CSV Reports	Manual copy-paste from tables	Tedious, especially for daily/weekly reports
📈 Scalability	Hard to manage growing data	Doesn’t scale with data volume or frequency
👥 Collaboration	Static, offline Excel files	No live data access or integration with dashboards
🔁 Repeatability	Have to do it all over again next time	Wastes time, lacks consistency
⏱ Real-time	Delays due to human bottleneck	Missed business opportunities

🧠 Alternative (Less Efficient) Ways vs Automation
Method	How It Works	Limitation
Manual BigQuery UI	Go to BigQuery console → run query → download CSV	No reuse, not scheduled
Google Sheets + BigQuery Add-on	Pull BigQuery data into Sheets	Limited by Sheets size & performance
Excel + Connector	Use Excel’s BigQuery plugin	Needs setup, not very flexible, still manual
Ad-hoc scripts	Run occasional SQL + Python scripts	Easy to forget, inconsistent results

✅ Benefits of Your Automation Setup
Using Python + BigQuery + Scheduled Reports allows:

Feature	Benefit
🕒 Automation	Save time, reduce human error
📈 Scalability	Works even as your data grows
🎯 Accuracy	Consistent logic, no manual errors
🔁 Repeatable	Run daily, weekly, or monthly
📤 Output to CSV	Easy to share or feed into dashboards
📊 Extendable	Add graphs, dashboards, or ML later

💡 Summary
Without Automation ❌	With Automation ✅
Tedious, error-prone	Fast, reliable, repeatable
No live integration	Can scale to dashboards & ML
High maintenance	Fully scriptable & schedulable

🔁 TL;DR:
Not automating means more manual work, more errors, and limited scalability.
Your current setup replaces all that with a robust, repeatable, and scalable solution ideal for real businesses or data teams.
