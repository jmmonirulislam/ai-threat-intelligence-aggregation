# ai-threat-intelligence-aggregation
A lightweight Python-based prototype for aggregating and categorizing AI-related cybersecurity threats using sources such as MITRE ATLAS, CISA advisories, and academic research.
# AI Threat Intelligence Aggregation and Categorization for Securing AI Systems

## Overview
This project is a lightweight Python-based prototype designed to organize and categorize AI-related cybersecurity threats from multiple public sources. The project focuses on improving understanding of threats targeting artificial intelligence systems by grouping them into structured categories.

The project was developed as part of the CYBR 472 semester project and focuses on AI security concepts, threat modeling, and defensive analysis rather than production-level automation.

---

## Project Goals
The main goal of this project is to collect and organize AI-related threat intelligence in a simple and understandable format. The system helps distinguish between:

- Hypothetical Threats
- Demonstrated Threats
- Active Exploitation

This categorization helps defenders better understand the maturity and severity of AI-related threats.

---

## Data Sources
The prototype references publicly available threat intelligence and research sources including:

- MITRE ATLAS
- CISA Advisories
- Academic Research Papers
- Security Research Articles
- AI Security Frameworks

---

## Technologies Used
- Python
- JSON
- CSV
- Google Colab
- GitHub

---

## Features
- AI threat categorization
- Structured threat organization
- Simple dataset generation
- Basic table-based output
- Lightweight prototype design

---

## Threat Categories

### Hypothetical
Threats discussed conceptually or theoretically in research literature without confirmed real-world exploitation.

### Demonstrated
Threats validated through proof-of-concept demonstrations, research experiments, or controlled testing environments.

### Active Exploitation
Threats observed or reported in real-world attacks, incident reports, or security advisories.

---

## Project Structure

```bash
data/                 # Sample threat datasets
scripts/              # Python scripts
output/               # Generated outputs
screenshots/          # Project screenshots
