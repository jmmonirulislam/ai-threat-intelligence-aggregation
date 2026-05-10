import json

with open("../data/sample_threats.json", "r") as file:
    threats = json.load(file)

print("Loaded Threat Data")

for threat in threats:
    print(threat["threat"], "-", threat["category"])
