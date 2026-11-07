
import os
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# PYTHON DATA ANALYSIS APPLICATION
# Internship Week 4 - Module 04
# =====================================

DATA_FOLDER = "data"
OUTPUT_FOLDER = "outputs"

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

DATA_FILE = os.path.join(DATA_FOLDER, "students.csv")


# 1. CREATE SAMPLE DATASET
def create_dataset():
    if not os.path.exists(DATA_FILE):
        data = {
            "Student": [
                "Rahul", "Aman", "Priya", "Neha",
                "Rohan", "Anjali", "Karan", "Simran",
                "Arjun", "Sneha"
            ],
            "Age": [20, 21, 19, 20, 22, 21, 20, 19, 22, 21],
            "Course": [
                "BTech", "BCA", "BTech", "BBA",
                "BCA", "BTech", "BBA", "BCA",
                "BTech", "BBA"
            ],
            "Marks": [85, 78, 92, 65, 74, 88, 56, 81, 95, 72],
            "Attendance": [90, 85, 95, 70, 80, 92, 65, 88, 98, 75]
        }

        df = pd.DataFrame(data)
        df.to_csv(DATA_FILE, index=False)
        print("Sample dataset created successfully!")


# 2. LOAD DATASET
def load_dataset():
    try:
        df = pd.read_csv(DATA_FILE)
        print("\nDataset loaded successfully!")
        print(df.head())
        return df

    except FileNotFoundError:
        print("Dataset file not found.")
        return pd.DataFrame()

    except Exception as error:
        print("Error loading dataset:", error)
        return pd.DataFrame()


# 3. DATA CLEANING
def clean_data(df):
    if df.empty:
        return df

    print("\n--- DATA CLEANING ---")

    print("Missing values before cleaning:")
    print(df.isnull().sum())

    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(
            df[column].median()
        )

    for column in df.select_dtypes(
        include="object"
    ).columns:
        df[column] = df[column].fillna("Unknown")

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print("\nDuplicates removed.")
    return df


# 4. DATA ANALYSIS
def analyze_data(df):
    if df.empty:
        return

    print("\n--- DATA ANALYSIS ---")

    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nAverage Marks:")
    print(df["Marks"].mean())

    print("\nHighest Marks:")
    print(df["Marks"].max())

    print("\nLowest Marks:")
    print(df["Marks"].min())

    print("\nCourse-wise Average Marks:")
    print(df.groupby("Course")["Marks"].mean())

    print("\nStudent Performance:")
    print(df[["Student", "Marks"]].sort_values(
        by="Marks", ascending=False
    ))


# 5. NUMPY OPERATIONS
def numpy_analysis(df):
    if df.empty:
        return

    print("\n--- NUMPY ANALYSIS ---")

    marks = np.array(df["Marks"])

    print("Marks Array:", marks)
    print("Mean:", np.mean(marks))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
    print("Standard Deviation:", np.std(marks))


# 6. DATA VISUALIZATION
def visualize_data(df):
    if df.empty:
        return

    print("\n--- GENERATING CHARTS ---")

    sns.set_theme(style="whitegrid")

    # Bar Chart
    plt.figure(figsize=(9, 5))
    sns.barplot(
        data=df,
        x="Student",
        y="Marks"
    )
    plt.title("Student Marks Comparison")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_FOLDER, "marks_chart.png")
    )
    plt.close()

    # Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(
        data=df,
        x="Marks",
        bins=5,
        kde=True
    )
    plt.title("Distribution of Student Marks")
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_FOLDER, "marks_distribution.png")
    )
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Attendance",
        y="Marks",
        hue="Course",
        s=100
    )
    plt.title("Attendance vs Marks")
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_FOLDER, "attendance_vs_marks.png")
    )
    plt.close()

    print("All charts saved in outputs folder.")


# 7. REST API AND JSON PROCESSING
def fetch_api_data():
    print("\n--- REST API DATA ---")

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        api_data = response.json()

        print("API data fetched successfully!")
        print("Total users:", len(api_data))

        # Process JSON response
        users = []

        for user in api_data:
            users.append({
                "ID": user["id"],
                "Name": user["name"],
                "Email": user["email"],
                "City": user["address"]["city"],
                "Company": user["company"]["name"]
            })

        api_df = pd.DataFrame(users)

        # Save JSON data
        json_file = os.path.join(
            OUTPUT_FOLDER, "api_users.json"
        )

        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(api_data, file, indent=4)

        # Save processed API data
        api_df.to_csv(
            os.path.join(OUTPUT_FOLDER, "api_users.csv"),
            index=False
        )

        print("\nAPI User Data:")
        print(api_df.head())

        return api_df

    except requests.exceptions.RequestException as error:
        print("API connection error:", error)

    except (ValueError, KeyError, TypeError) as error:
        print("Error processing API data:", error)

    return pd.DataFrame()


# 8. GENERATE REPORT
def generate_report(df, api_df):
    if df.empty:
        print("Cannot generate report without dataset.")
        return

    report = []

    report.append("PYTHON DATA ANALYSIS REPORT")
    report.append("=" * 35)

    report.append(f"Total Students: {len(df)}")
    report.append(f"Average Marks: {df['Marks'].mean():.2f}")
    report.append(f"Highest Marks: {df['Marks'].max()}")
    report.append(f"Lowest Marks: {df['Marks'].min()}")
    report.append(
        f"Average Attendance: {df['Attendance'].mean():.2f}"
    )

    report.append("\nCourse-wise Average Marks:")

    course_average = df.groupby("Course")["Marks"].mean()

    for course, average in course_average.items():
        report.append(f"{course}: {average:.2f}")

    if not api_df.empty:
        report.append(
            f"\nTotal API Users Retrieved: {len(api_df)}"
        )

    report.append("\nConclusion:")
    report.append(
        "The dataset was loaded, cleaned and analyzed "
        "using Python libraries."
    )
    report.append(
        "Charts were generated to visualize student "
        "performance and attendance."
    )
    report.append(
        "REST API data was fetched and processed "
        "into JSON and CSV formats."
    )

    report_file = os.path.join(
        OUTPUT_FOLDER, "analysis_report.txt"
    )

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("\n".join(report))

    print("\n--- FINAL REPORT ---")
    print("\n".join(report))
    print("\nReport saved successfully!")


# 9. MAIN APPLICATION
def main():
    print("=" * 45)
    print("PYTHON DATA ANALYSIS APPLICATION")
    print("=" * 45)

    create_dataset()

    df = load_dataset()

    if df.empty:
        print("Application stopped due to missing data.")
        return

    df = clean_data(df)

    # Save cleaned dataset
    df.to_csv(
        os.path.join(OUTPUT_FOLDER, "cleaned_students.csv"),
        index=False
    )

    analyze_data(df)
    numpy_analysis(df)
    visualize_data(df)

    api_df = fetch_api_data()

    generate_report(df, api_df)

    print("\n===================================")
    print("DATA ANALYSIS APPLICATION COMPLETED")
    print("===================================")


if __name__ == "__main__":
    main()
      
