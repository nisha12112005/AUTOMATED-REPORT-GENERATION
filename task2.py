import pandas as pd
from fpdf import FPDF

# Read the data
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Score': [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

# Save it as CSV
df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv')

# Basic analysis
average_score = df['Score'].mean()
highest_score = df['Score'].max()
top_student = df[df['Score'] == highest_score]['Name'].values[0]

# Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Performance Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "", 12)

# Add Summary
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, f"Top Student: {top_student} with {highest_score}", ln=True)
pdf.ln(10)

# Add Table Header
pdf.set_font("Arial", "B", 12)
pdf.cell(40, 10, "Name", 1)
pdf.cell(40, 10, "Score", 1)
pdf.ln()

# Add Table Data
pdf.set_font("Arial", "", 12)
for _, row in df.iterrows():
    pdf.cell(40, 10, row['Name'], 1)
    pdf.cell(40, 10, str(row['Score']), 1)
    pdf.ln()

# Save the report
pdf.output("report.pdf")
print("✅ Report generated as report.pdf")
