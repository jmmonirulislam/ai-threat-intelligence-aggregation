import json

print("AI Threat Intelligence Aggregation Prototype")

sample_threats = [
    {
        "name": "Prompt Injection",
        "category": "Demonstrated",
        "source": "MITRE ATLAS"
    },
    {
        "name": "Training Data Poisoning",
        "category": "Hypothetical",
        "source": "Research Literature"
    },
    {
        "name": "Model Evasion",
        "category": "Active Exploitation",
        "source": "CISA Advisory"
    }
]

print(json.dumps(sample_threats, indent=4))
