# 📊 DDoS SHAP Pilot Analysis

> Pilot exploratory analysis of DDoS network traffic data — inspecting dataset structure, class distribution, and establishing an initial workflow for SHAP-based explainability on tree-based models.

![Status](https://img.shields.io/badge/status-pilot%20%2F%20exploratory-orange)
![Python](https://img.shields.io/badge/python-3.x-blue)

---

## Overview

This repository contains a **pilot exploratory analysis** of distributed denial-of-service (DDoS) network traffic data. It is an early-stage analysis intended to inform and refine subsequent modelling and explainability experiments in a larger research project.

No final models or performance claims are made at this stage.

---

## Objectives

- Inspect the structure and dimensionality of a DDoS traffic dataset
- Examine the distribution of benign and attack traffic labels
- Perform basic preprocessing and binary label creation
- Prepare the groundwork for applying SHAP explanations to tree-based models
- Identify potential data quality or imbalance issues before full experimentation

---

## Repository Structure
ddos-shap-pilot-analysis/
│
├── pilot_shap_stability.py   # Pilot analysis script
├── data/
│   └── README.md             # Dataset instructions (raw data not included)
├── .gitignore                # Excludes large/raw data files
└── README.md                 # Project overview (this file)

---

## Dataset

The raw dataset is **not included** in this repository due to file size limits and good research practice.

Obtain the dataset from publicly available sources:
- [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)
- [CIC-DDoS2019](https://www.unb.ca/cic/datasets/ddos-2019.html)

After downloading, place the file at:
data/ddos.csv

---

## Scope

**Included in this repository:**
- Exploratory data inspection
- Label analysis and preprocessing
- Explainability pipeline preparation

**Deferred to later research stages:**
- Final model training or optimisation
- Comparative algorithm evaluation
- Full SHAP stability experiments

---

## Tools and Technologies

| Tool | Status |
|------|--------|
| Python | Active |
| pandas | Active |
| SHAP | Planned |
| XGBoost / LightGBM | Planned |

---

## Status

🚧 **Pilot / Exploratory Stage** — preliminary analysis only. Does not represent final research implementation or findings.

---

## Author

**Isha Atif**  
MRes Applied Artificial Intelligence  
Focus: Explainable AI, DDoS detection, and trustworthy machine learning