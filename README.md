# AAI551-Final-Project

# Earthquake Analysis System

## Team Members
- Owusu Kwaku — okwaku@stevens.edu — 20011160
- Corinthian Bray — cbray@stevens.edu — 20014276
- Nolan-Hatchell McNeil — nhatchel@stevens.edu — 20015770

## Project Description
The Earthquake Analysis System is a Python-based project that analyzes real earthquake data from the United States Geological Survey (USGS). The system reads earthquake records from a CSV file, creates earthquake objects, classifies earthquakes by severity, computes risk scores, identifies clusters of nearby earthquake events, and generates visualizations to help users better understand seismic activity.

This project is designed to transform raw seismic data into more meaningful analytical insights using object-oriented programming, functions, file input/output, exception handling, testing, and data visualization.

## Features
- Loads earthquake data from a CSV file
- Uses a base class `EarthquakeEvent` to represent seismic events
- Uses a subclass `AnalyzedEarthquake` that extends the base class with analytical attributes
- Classifies earthquake severity based on magnitude
- Computes earthquake risk scores using magnitude, depth, and population density
- Clusters nearby earthquakes to identify seismic hotspots
- Uses Pandas for data handling
- Uses Matplotlib for visualizations
- Saves processed analysis results to a CSV file
- Includes exception handling for bad input files or invalid values
- Includes Pytest test cases for core logic

## Project Structure
```text
earthquake-analysis/
│
├── data/
│   └── earthquakes.csv
├── src/
│   ├── models.py  (Corinthian Bray)
│   ├── analysis.py (Nolan Hatchell-McNeil)
│   ├── io_utils.py (Owusu Kwaku)
│   └── main.py (Owusu Kwaku)
├── tests/
│   └── test_project.py
├── notebook/
│   └── earthquake_analysis.ipynb
├── results/
│   └── analysis_results.csv
└── README.md 

## How to Run the Project
1. Download or clone the project files.
2. Open a terminal in the project folder.
3. Install the required libraries:

python -m pip install pandas matplotlib pytest

4. Place the earthquake dataset in the `data` folder and name it `earthquakes.csv`.
5. Run the program with:

python src/main.py
