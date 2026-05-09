import csv

print("Categorized AI Threats")

with open("../output/categorized_threats.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
