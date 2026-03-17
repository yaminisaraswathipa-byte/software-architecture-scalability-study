import csv
import re
import subprocess
import sys

# This is the Python file we want to analyze with Radon.
TARGET_FILE = "example.py"


# This helper function runs a terminal command and returns its output as text.
def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )

    # If the command fails, show the error and stop the script.
    if result.returncode != 0:
        print("Command failed:")
        print(command)
        print(result.stderr)
        sys.exit(1)

    return result.stdout


# Run Radon raw metrics command.
raw_output = run_command(f"radon raw {TARGET_FILE}")

# Run Radon cyclomatic complexity command.
complexity_output = run_command(f"radon cc {TARGET_FILE} -s -a")

# Run Radon maintainability index command.
maintainability_output = run_command(f"radon mi {TARGET_FILE} -s")


# Save the raw command outputs into text files.
with open("raw_metrics.txt", "w", encoding="utf-8") as file:
    file.write(raw_output)

with open("complexity_metrics.txt", "w", encoding="utf-8") as file:
    file.write(complexity_output)

with open("maintainability_metrics.txt", "w", encoding="utf-8") as file:
    file.write(maintainability_output)


# Extract LOC from raw_metrics.txt output.
loc_match = re.search(r"LOC:\s*(\d+)", raw_output)
loc = int(loc_match.group(1)) if loc_match else None

# Extract average cyclomatic complexity numeric value from complexity output.
complexity_match = re.search(r"Average complexity:\s*[A-F]\s*\(([\d.]+)\)", complexity_output)
cyclomatic_complexity = float(complexity_match.group(1)) if complexity_match else None

# Extract maintainability grade and numeric score from maintainability output.
# Example expected format:
# example.py - A (100.00)
mi_grade_match = re.search(r"-\s*([A-F])", maintainability_output)
maintainability_grade = mi_grade_match.group(1) if mi_grade_match else None

mi_score_match = re.search(r"\(([\d.]+)\)", maintainability_output)
maintainability_score = float(mi_score_match.group(1)) if mi_score_match else None


# Write the final structured results to CSV.
with open("metrics.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "file",
        "loc",
        "cyclomatic_complexity",
        "maintainability_score",
        "maintainability_grade"
    ])
    writer.writerow([
        TARGET_FILE,
        loc,
        cyclomatic_complexity,
        maintainability_score,
        maintainability_grade
    ])

print("Metrics generated successfully.")
print("Created files:")
print("- raw_metrics.txt")
print("- complexity_metrics.txt")
print("- maintainability_metrics.txt")
print("- metrics.csv")
