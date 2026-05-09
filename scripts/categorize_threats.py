def categorize_threat(threat_name):
    categories = {
        "Prompt Injection": "Demonstrated",
        "Data Poisoning": "Hypothetical",
        "Model Evasion": "Active Exploitation"
    }

    return categories.get(threat_name, "Unknown")


print(categorize_threat("Prompt Injection"))
