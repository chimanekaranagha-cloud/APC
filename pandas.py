import pandas as pd
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Riya', 'Neha', 'Rahul', 'Sneha'],
    'Python': [85, 70, 90, 65, 80],
    'DBMS': [80, 75, 85, 70, 90],
    'Maths': [90, 80, 95, 60, 85]
}
df = pd.DataFrame(data)
print("Student Data:")
print(df)
df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
df['Average'] = df['Total'] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents Scoring Above 75%:")
print(df[df['Average'] > 75])





import pandas as pd
data = {
    'Employee_ID': [1, 2, 3, 4, 5],
    'Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Neha'],
    'Department': ['CSE', 'IT', 'HR', 'CSE', 'IT'],
    'Salary': [45000, 60000, 55000, 70000, 40000],
    'Experience': [2, 5, 3, 7, 1]
}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print("\nEmployees with Salary Above 50000:")
print(df[df['Salary'] > 50000])
print("\nAverage Salary:")
print(df['Salary'].mean())
print("\nHighest Salary:")
print(df['Salary'].max())
print("\nEmployee with Highest Experience:")
print(df.loc[df['Experience'].idxmax()])




import pandas as pd
data = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'Price': [50000, 500, 1500, 12000],
    'Quantity': [2, 10, 5, 3]
}
df = pd.DataFrame(data)
df['Total_Amount'] = df['Price'] * df['Quantity']
print("Product Data:")
print(df)
print("\nProduct with Highest Total Sales:")
print(df.loc[df['Total_Amount'].idxmax()])





import pandas as pd
data = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Name': ['Amit', 'Riya', 'Neha', 'Rahul', 'Sneha'],
    'Age': [65, 45, 70, 30, 55],
    'Disease': ['Diabetes', 'Fever', 'Heart', 'Cold', 'Cancer'],
    'Medical_Charges': [60000, 20000, 80000, 15000, 55000]
}
df = pd.DataFrame(data)
print("Patient Data:")
print(df)
print("\nPatients Above 60 Years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Charges:")
print(df['Medical_Charges'].mean())
print("\nMaximum Medical Charges:")
print(df['Medical_Charges'].max())
print("\nPatients with Charges Above 50000:")
print(df[df['Medical_Charges'] > 50000])






import pandas as pd

data = {
    'Order_ID': [101, 102, 103, 104],
    'Customer': ['Amit', 'Riya', 'Neha', 'Rahul'],
    'Product': ['Laptop', 'Mobile', 'Mouse', 'Tablet'],
    'Quantity': [2, 1, 5, 3],
    'Price': [4000, 6000, 500, 2000],
    'Discount': [500, 200, 100, 300]
}

df = pd.DataFrame(data)
df['Final_Amount'] = df['Quantity'] * df['Price'] - df['Discount']
print("All Orders:")
print(df)
print("\nOrders Above 5000:")
print(df[df['Final_Amount'] > 5000])
print("\nHighest Value Order:")
print(df.loc[df['Final_Amount'].idxmax()])
print("\nAverage Order Value:")
print(df['Final_Amount'].mean())




import pandas as pd
data = {
    'Order_ID': [101, 102, 103, 104],
    'Customer': ['Amit', 'Riya', 'Neha', 'Rahul'],
    'Product': ['Laptop', 'Mobile', 'Mouse', 'Tablet'],
    'Quantity': [2, 1, 5, 3],
    'Price': [4000, 6000, 500, 2000],
    'Discount': [500, 200, 100, 300]
}
df = pd.DataFrame(data)
df['Final_Amount'] = df['Quantity'] * df['Price'] - df['Discount']
print("All Orders:")
print(df)
print("\nOrders Above 5000:")
print(df[df['Final_Amount'] > 5000])
print("\nHighest Value Order:")
print(df.loc[df['Final_Amount'].idxmax()])
print("\nAverage Order Value:")
print(df['Final_Amount'].mean())




import pandas as pd
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Riya', 'Neha', 'Rahul', 'Sneha'],
    'Department': ['CSE', 'IT', 'CSE', 'ENTC', 'IT'],
    'Total_Classes': [100, 100, 100, 100, 100],
    'Classes_Attended': [80, 70, 90, 60, 75]
}
df = pd.DataFrame(data)
df['Attendance_Percentage'] = (
    df['Classes_Attended'] / df['Total_Classes']
) * 100
print("Student Attendance:")
print(df)
print("\nStudents Below 75% Attendance:")
print(df[df['Attendance_Percentage'] < 75])





import pandas as pd
data = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'Price': [50000, 500, 1500, 12000],
    'Quantity': [2, 10, 5, 3]
}
df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']
print("Product Data:")
print(df)
print("\nProducts with Sales Above 10000:")
print(df[df['Total_Sales'] > 10000])
print("\nProduct with Maximum Sales:")
print(df.loc[df['Total_Sales'].idxmax()])
print("\nAverage Sales:")
print(df['Total_Sales'].mean())



import pandas as pd
marks = {
    'Amit': 85,
    'Riya': 90,
    'Neha': 70,
    'Rahul': 65,
    'Sneha': 95
}
s = pd.Series(marks)
print("Student Marks:")
print(s)
print("\nMarks of Riya:")
print(s['Riya'])
print("\nMaximum Marks:")
print(s.max())
print("\nMinimum Marks:")
print(s.min())
print("\nAverage Marks:")
print(s.mean())
print("\nStudents Scoring Above 75:")
print(s[s > 75])





import pandas as pd
salary = {
    'Amit': 45000,
    'Riya': 60000,
    'Neha': 55000,
    'Rahul': 70000,
    'Sneha': 40000
}
s = pd.Series(salary)
print("Employee Salaries:")
print(s)
print("\nHighest Salary:")
print(s.max())
print("\nLowest Salary:")
print(s.min())
print("\nAverage Salary:")
print(s.mean())
print("\nEmployees Earning Above 50000:")
print(s[s > 50000])



import pandas as pd
prices = {
    'Laptop': 50000,
    'Mouse': 500,
    'Keyboard': 1500,
    'Monitor': 12000
}
s = pd.Series(prices)
print("Product Prices:")
print(s)
s = s * 1.10
print("\nPrices After 10% Increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax())
print("\nProducts Costing Above 1000:")
print(s[s > 1000])




import pandas as pd
ages = {
    101: 65,
    102: 45,
    103: 70,
    104: 30,
    105: 55
}
s = pd.Series(ages)
print("Patient Ages:")
print(s)
print("\nAverage Age:")
print(s.mean())
print("\nOldest Patient:")
print(s.idxmax(), s.max())
print("\nYoungest Patient:")
print(s.idxmin(), s.min())
print("\nPatients Above 60 Years:")
print(s[s > 60])





import pandas as pd
attendance = {
    'Amit': 85,
    'Riya': 70,
    'Neha': 95,
    'Rahul': 65,
    'Sneha': 92
}
s = pd.Series(attendance)
print("Student Attendance:")
print(s)
print("\nAverage Attendance:")
print(s.mean())
print("\nStudents Below 75%:")
print(s[s < 75])
print("\nStudents Above 90%:")
print(s[s > 90])
print("\nHighest Attendance:")
print(s.max())



import pandas as pd
df = pd.read_csv('students.csv')
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
df['Average'] = df['Total'] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with Average Above 75:")
print(df[df['Average'] > 75])
print("\nStudent with Highest Average:")
print(df.loc[df['Average'].idxmax()])
print("\nSubject-wise Average:")
print(df[['Python', 'DBMS', 'Maths']].mean())



import pandas as pd

df = pd.read_csv('employees.csv')

print("Employee Data:")
print(df)

print("\nEmployees from CSE Department:")
print(df[df['Department'] == 'CSE'])

print("\nAverage Salary:")
print(df['Salary'].mean())

print("\nHighest Salary:")
print(df['Salary'].max())

print("\nLowest Salary:")
print(df['Salary'].min())

print("\nEmployees with Salary Above 50000:")
print(df[df['Salary'] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby('Department')['Salary'].mean())




import pandas as pd

df = pd.read_csv('patients.csv')

print("Patient Data:")
print(df)

print("\nPatients Above 60 Years:")
print(df[df['Age'] > 60])

print("\nAverage Medical Expense:")
print(df['Medical_Expense'].mean())

print("\nPatient with Highest Medical Expense:")
print(df.loc[df['Medical_Expense'].idxmax()])

print("\nDisease-wise Patient Count:")
print(df['Disease'].value_counts())

print("\nPatients with Medical Expense Above 50000:")
print(df[df['Medical_Expense'] > 50000])