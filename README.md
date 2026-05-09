# AI Threat Intelligence Aggregation and Categorization for Securing AI Systems

## Overview
This project is a lightweight Python-based prototype designed to organize and categorize AI-related cybersecurity threats from multiple public sources. The project focuses on improving understanding of threats targeting artificial intelligence systems by grouping them into structured categories.

The project was developed as part of the CYBR 472 semester project and focuses on AI security concepts, threat modeling, and defensive analysis rather than production-level automation.

## Project Goals
The main goal of this project is to collect and organize AI-related threat intelligence in a simple and understandable format. The system helps distinguish between:

- Hypothetical Threats
- Demonstrated Threats
- Active Exploitation

This categorization helps defenders better understand the maturity and severity of AI-related threats.

## Data Sources
The prototype references publicly available threat intelligence and research sources including:

- MITRE ATLAS
- CISA Advisories
- Academic Research Papers
- Security Research Articles
- AI Security Frameworks

## Technologies Used
- Python
- JSON
- CSV
- Google Colab
- GitHub

## Features
- AI threat categorization
- Structured threat organization
- Simple dataset generation
- Basic table-based output
- Lightweight prototype design

## Threat Categories

### Hypothetical
Threats discussed conceptually or theoretically in research literature without confirmed real-world exploitation.

### Demonstrated
Threats validated through proof-of-concept demonstrations, research experiments, or controlled testing environments.

### Active Exploitation
Threats observed or reported in real-world attacks, incident reports, or security advisories.

## Repository Structure

```bash
data/
│── sample_threats.json

scripts/
│── main.py
│── categorize_threats.py
│── generate_table.py

screenshots/
│── output_example.jpg

output/
│── categorized_threats.csv
```

## How to Run

Run the main prototype script:

```bash
python scripts/main.py
```

Run the table generation script:

```bash
python scripts/generate_table.py
```

## Future Improvements
- Automated threat ingestion from MITRE ATLAS
- Real-time advisory updates
- Dashboard visualization
- Improved threat classification logic
- Integration with additional AI security datasets

## Educational Purpose
This project was created for academic and research purposes as part of the CYBR 472 semester project. The repository demonstrates a simplified prototype for organizing and categorizing AI-related cybersecurity threats.

## Author
Monirul Islam  
California State University
