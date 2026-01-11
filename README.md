📊 DDoS SHAP Pilot Analysis
Overview

This repository contains a pilot exploratory analysis of distributed denial-of-service (DDoS) network traffic data. The aim of this pilot is to inspect dataset structure, examine class distribution, and establish an initial workflow for applying SHAP-based explainability to tree-based machine learning models.

This work represents an early-stage analysis intended to inform and refine subsequent modelling and explainability experiments in a larger research project.

Objectives of the Pilot Study

The specific goals of this pilot analysis are to:

Inspect the structure and dimensionality of a DDoS traffic dataset
Examine the distribution of benign and attack traffic labels
Perform basic preprocessing and binary label creation
Prepare the groundwork for applying SHAP explanations to tree-based models
Identify potential data quality or imbalance issues before full experimentation
No final models or performance claims are made at this stage.

Repository Structure
ddos-shap-pilot-analysis/
│
├── pilot_shap_stability.py   # Pilot analysis script
├── data/
│   └── README.md             # Dataset instructions (raw data not included)
├── .gitignore                # Excludes large/raw data files
└── README.md                 # Project overview (this file)

Dataset Notice

The raw DDoS dataset used in this pilot analysis is not included in the repository due to GitHub file size limits and good research practice.

The dataset can be obtained from publicly available intrusion detection datasets such as:

CICIDS2017
CIC-DDoS2019

After downloading, place the dataset in the following location:
data/ddos.csv

Methodological Scope

This repository focuses on:

Exploratory data inspection
Label analysis and preprocessing
Explainability pipeline preparation

It does not include:

Final model training or optimisation
Comparative algorithm evaluation
Full SHAP stability experiments
Those components are intentionally deferred to later stages of the research.

Tools and Technologies

Python
pandas
SHAP (planned integration)
Tree-based machine learning models (planned)

Status

🚧 Pilot / Exploratory Stage

This repository reflects preliminary analysis only and does not represent the final research implementation or findings.

Author

Isha Atif
MRes Applied Artificial Intelligence
Focus: Explainable AI, DDoS detection, and trustworthy machine learning