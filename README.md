---
license: mit
language:
- en
pretty_name: Purple Team Cybersecurity Dataset
---

# Purple Team Cybersecurity Dataset

<!-- Hugging Face Metadata -->
<!-- language: other -->
<!-- license: mit -->
<!-- datasets: canstralian/Purple-Team-Cybersecurity-Dataset -->

<!-- Badges -->
[![Build Status](https://img.shields.io/github/actions/workflow/status/canstralian/Purple-Team-Cybersecurity-Dataset/ci.yml)](https://github.com/canstralian/Purple-Team-Cybersecurity-Dataset/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Dataset Card for Purple Team Cybersecurity Dataset

**Dataset Summary**

The Purple Team Cybersecurity Dataset is a comprehensive collection of events that amalgamates Red Team (attack) and Blue Team (defense) data. This dataset is designed to facilitate research and development in cybersecurity, particularly in understanding and analyzing the interplay between offensive and defensive strategies. It includes standardized fields such as timestamps, IP addresses, MITRE ATT&CK IDs, tool names, and event descriptions, providing a balanced perspective of both attack and defense scenarios.

### Dataset Details

**Dataset Description**

This dataset was curated by combining existing Red Team and Blue Team datasets, normalizing and standardizing the data to ensure consistency. Each event is labeled as either “Attack” or “Defense” and is mapped to the corresponding MITRE ATT&CK tactics. The dataset aims to support cybersecurity research by providing a balanced and comprehensive view of both offensive and defensive events.
- Curated by: Canstralian
- Language(s) (NLP): Not Applicable
- License: MIT License

Dataset Sources
- Repository: [https://github.com/canstralian/Purple-Team-Cybersecurity-Dataset](https://github.com/canstralian/Purple-Team-Cybersecurity-Dataset)
- Paper: [More Information Needed (Optional)]

Uses

Direct Use

This dataset is intended for use in cybersecurity research, including but not limited to:
- Analyzing attack and defense patterns 
- Developing and testing intrusion detection systems
- Training machine learning models for threat detection

Out-of-Scope Use

The dataset is not suitable for:
   • Real-time threat monitoring in production environments
   • Any application involving sensitive or personally identifiable information

Dataset Structure

The dataset comprises events with the following fields:
   • Timestamp: ISO 8601 formatted date and time
   • Source_IP: Validated source IP address
   • Destination_IP: Validated destination IP address
   • MITRE_ATT&CK_ID: Standardized MITRE ATT&CK technique ID
   • Tool_Name: Standardized name of the tool used
   • Event_Description: Detailed description of the event
   • Event_Type: Label indicating “Attack” or “Defense”
   • MITRE_Tactic: Mapped MITRE ATT&CK tactic

Dataset Creation

Curation Rationale

The dataset was created to provide a balanced and comprehensive resource for cybersecurity professionals and researchers, enabling the study of both attack and defense mechanisms within a unified framework.

Source Data

Data Collection and Processing

Data was collected from existing Red Team and Blue Team datasets, followed by normalization and standardization processes to ensure consistency across fields. Events were labeled and mapped to MITRE ATT&CK tactics to facilitate structured analysis.

Who are the source data producers?

The original data was produced by various cybersecurity teams and organizations engaged in offensive and defensive security operations.

Annotations

Annotation process

Events were labeled as “Attack” or “Defense” based on their origin and nature. Each event was mapped to the corresponding MITRE ATT&CK tactic using a predefined mapping.

Who are the annotators?

The annotation was performed by cybersecurity experts with experience in both offensive and defensive operations.

Personal and Sensitive Information

The dataset does not contain any personal or sensitive information. All IP addresses have been validated to ensure they do not correspond to real-world entities.

Bias, Risks, and Limitations

While efforts have been made to balance the dataset, there may still be inherent biases due to the nature of the source data. Users should be aware of these potential biases and exercise caution when interpreting the results.

Recommendations

Users should be made aware of the risks, biases, and limitations of the dataset. More information needed for further recommendations.

Citation

BibTeX:

[More Information Needed]

APA:

[More Information Needed]

Glossary
   • MITRE ATT&CK: A globally accessible knowledge base of adversary tactics and techniques based on real-world observations.

More Information

[More Information Needed]

Dataset Card Authors

**Author**: Canstralian
- **GitHub**: [https://github.com/canstralian](https://github.com/canstralian)
- **Hugging Face**: [https://huggingface.co/canstralian](https://huggingface.co/canstralian)

Dataset Card Contact

**Contact Information**: [Your Contact Information (email or other contact)]

## Running Tests

To ensure the integrity of the data and the functionality of the scripts, we have included a suite of automated tests. You can run these tests using `pytest`.

### Instructions

1. **Install Dependencies**:
   Ensure you have all the necessary dependencies installed. You can install them using `pip`:

   ```bash
   pip install -r requirements.txt