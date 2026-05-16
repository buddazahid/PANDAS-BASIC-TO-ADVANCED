# ============================================
# PANDAS BASIC TO ADVANCED - EASY GUIDE
# ============================================

# Install pandas
# pip install pandas

# Import pandas
import pandas as pd

# ============================================
# 1. CREATE DATAFRAME
# ============================================

data = {
    "Name": ["Zahid", "Ali", "Sara", "John"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# ============================================
# 2. READ CSV FILE
# ============================================

# df = pd.read_csv("students.csv")

# ============================================
# 3. VIEW DATA
# ============================================

print(df.head())     # First 5 rows
print(df.tail())     # Last 5 rows
print(df.shape)      # Rows and columns
print(df.columns)    # Column names
print(df.info())     # Data information

# ============================================
# 4. SELECT DATA
# ============================================

print(df["Name"])          # Single column
print(df[["Name", "Age"]]) # Multiple columns

# ============================================
# 5. FILTER DATA
# ============================================

print(df[df["Marks"] > 80])

# ============================================
# 6. ADD NEW COLUMN
# ============================================

df["Result"] = ["Pass", "Pass", "Pass", "Pass"]

print(df)

# ============================================
# 7. UPDATE VALUES
# ============================================

df.loc[0, "Marks"] = 95

print(df)

# ============================================
# 8. DELETE COLUMN
# ============================================

df = df.drop("Result", axis=1)

print(df)

# ============================================
# 9. SORT DATA
# ============================================

print(df.sort_values(by="Marks", ascending=False))

# ============================================
# 10. FIND NULL VALUES
# ============================================

print(df.isnull())

# ============================================
# 11. FILL NULL VALUES
# ============================================

df["Marks"] = df["Marks"].fillna(0)

# ============================================
# 12. GROUP BY
# ============================================

data2 = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 45000, 47000]
}

df2 = pd.DataFrame(data2)

print(df2.groupby("Department")["Salary"].mean())

# ============================================
# 13. MERGE DATAFRAMES
# ============================================

student = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Zahid", "Ali"]
})

marks = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [90, 85]
})

merged = pd.merge(student, marks, on="ID")

print(merged)

# ============================================
# 14. SAVE CSV FILE
# ============================================

# df.to_csv("output.csv", index=False)

# ============================================
# 15. APPLY FUNCTION
# ============================================

df["Bonus"] = df["Marks"].apply(lambda x: x + 5)

print(df)

# ============================================
# 16. UNIQUE VALUES
# ============================================

print(df["Age"].unique())

# ============================================
# 17. VALUE COUNTS
# ============================================

print(df["Age"].value_counts())

# ============================================
# 18. ADVANCED QUERY
# ============================================

result = df.query("Marks > 80 and Age >= 21")

print(result)

# ============================================
# 19. PIVOT TABLE
# ============================================

pivot = df2.pivot_table(
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print(pivot)

# ============================================
# 20. EXPORT TO EXCEL
# ============================================

# df.to_excel("students.xlsx", index=False)

# ============================================
# END OF PANDAS GUIDE
# ============================================

print("Pandas Learning Completed!")