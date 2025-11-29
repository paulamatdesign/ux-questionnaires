# ux-questionnaires

A Streamlit application to compute, visualize, and export key UX questionnaire scores such as **SUS (System Usability Scale)**, **SUS item breakdowns**, and related computed metrics.  
The app allows users to upload raw data, automatically compute results, and explore them across different views.

## Features

- Upload raw questionnaire data (CSV, XLSX)
- Compute SUS score automatically
- Display computed scores per participant
- Mean, distribution and reliability metrics
- Multipage UI:
  - SUS Score
  - Computed Data
  - Raw Data
- Export results
- Simple and intuitive UX

## Starter commands

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py

## Licence

This project is licensed under the MIT License.
See the LICENSE file for details.
