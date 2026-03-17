import csv

# Hardcoded values from Radon results
file_name = "example.py"
loc = 23
cyclomatic_complexity = 2.66
maintainability_index = "A"

# Write results to CSV
with open("metrics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["file", "loc", "cyclomatic_complexity", "maintainability_index"])
    writer.writerow([file_name, loc, cyclomatic_complexity, maintainability_index])

print("metrics.csv generated successfully")
