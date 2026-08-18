import sys
import csv
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
students = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            students.append({
                "first":first_name,
                "last":last_name, 
                "house":row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline = "") as file2:
    fieldsname = ["first","last","house"]
    writer = csv.DictWriter(file2, fieldnames=fieldsname)
    writer.writeheader()
    for student in students:
        writer.writerow(student)