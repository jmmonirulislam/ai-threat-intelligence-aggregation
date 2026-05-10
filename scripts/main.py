import json

print("AI Threat Intelligence Aggregation Prototype")

with open("../data/sample_threats.json", "r") as file:
    threats = json.load(file)

print(json.dumps(threats, indent=4))
