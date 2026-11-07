
# Python Data Analysis Application

## Introduction

The Python Data Analysis Application is developed as part of Internship Week 4.

This project uses Python libraries to load, clean, analyze and visualize datasets. It also demonstrates how to consume REST APIs and process JSON data.

## Objectives

- Learn data analysis using NumPy and Pandas.
- Perform data cleaning and manipulation.
- Create visualizations using Matplotlib and Seaborn.
- Consume REST APIs using Python requests.
- Process JSON data.
- Generate a final data analysis report.

## Technologies Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Requests
- JSON
- REST API

## Project Features

1. Automatic sample dataset creation.
2. Dataset loading using Pandas.
3. Missing value handling.
4. Duplicate record removal.
5. Statistical data analysis.
6. NumPy calculations.
7. Data visualization.
8. REST API integration.
9. JSON data processing.
10. Automatic report generation.

## Project Structure

Python-Data-Analysis-Application/
|
|-- main.py
|-- README.md
|-- requirements.txt
|-- .gitignore
|
|-- data/
|   |-- students.csv
|
|-- outputs/
    |-- cleaned_students.csv
    |-- marks_chart.png
    |-- marks_distribution.png
    |-- attendance_vs_marks.png
    |-- api_users.json
    |-- api_users.csv
    |-- analysis_report.txt

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python main.py
```

## Dataset

The project creates a sample student dataset containing:

- Student names
- Age
- Course
- Marks
- Attendance

The dataset is stored in CSV format.

## Data Analysis

The application calculates:

- Average marks
- Highest marks
- Lowest marks
- Standard deviation
- Course-wise average marks
- Student performance

## Data Visualization

The project generates:

- Bar Chart: Student marks comparison.
- Histogram: Distribution of marks.
- Scatter Plot: Attendance versus marks.

## REST API Integration

The project uses the JSONPlaceholder REST API to retrieve sample user information.

API Endpoint:
https://jsonplaceholder.typicode.com/users

The API response is processed using JSON and Pandas and saved in CSV and JSON formats.

## Report Generation

The application automatically generates a report containing statistical results and analysis conclusions.

## Conclusion

This project helped me understand practical data analysis using Python. I learned how to work with NumPy, Pandas, Matplotlib and Seaborn, consume REST APIs, process JSON responses and generate reports.

**Internship Module:** Week 4 - Python Data & APIs
