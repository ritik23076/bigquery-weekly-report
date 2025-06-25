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

### ✅ 3. Scheduling the Script

You can use:

#### 🔹 On macOS/Linux:
Use `cron` to run the job daily or weekly:
```bash
0 9 * * 1 /path/to/run_report.sh >> /path/to/log.txt 2>&1
