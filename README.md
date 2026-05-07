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

## Team Contributions

### Corinthian Bray: Core classes and main program

- This can be your set.
- Initial project structure
- create folders: src, tests, notebook, data, results
- add starter files

Commit message:

- Set up project folder structure and starter files
- Base class
- add EarthquakeEvent
- include attributes and severity classification

Commit message:

- Added EarthquakeEvent class with severity classification
- Subclass
- add AnalyzedEarthquake
- inheritance from EarthquakeEvent

Commit message:

- Implemented AnalyzedEarthquake subclass with analysis fields
- Special methods
- add __str__()
- add __eq__()

Commit message:

- Added __str__ and __eq__ methods to earthquake classes
- Main program integration
- connect loading, analysis, and output in main.py

Commit message:
- Connected classes and analysis workflow in main program

### Nolan Hatchell-McNeil: Data handling and analysis
- This person can focus on the functions and data side.
- CSV loader
- create file loading logic
- read USGS CSV with pandas

Commit message:
- Added CSV loading for USGS earthquake dataset
- Custom exception handling
- add DataLoadError
- handle missing or bad files

Commit message:
- Added custom exception handling for invalid dataset input
- Risk score function
- create compute_risk_score()

Commit message:
- Implemented earthquake risk score calculation function
- Clustering function
- create cluster_earthquakes()

Commit message:
- Added clustering logic to identify earthquake hotspots
- Save results
- export processed results to CSV

Commit message:
- Added processed earthquake results export to CSV

### Owusu Kwaku: Notebook, testing, and documentation

- This person can handle demonstration and project polish.

- Pytest for severity
- add test for classify_severity()

-Commit message:

- Added pytest case for earthquake severity classification
- Pytest for risk score
- add test for compute_risk_score()

-Commit message:

- Added pytest case for earthquake risk score function
- Notebook setup
- create Jupyter notebook sections
- load data and demonstrate workflow

-Commit message:

- Created Jupyter notebook for earthquake analysis workflow
- Visualizations
- add histogram, bar chart, scatter plot

Commit message:
- Added earthquake data visualizations to notebook
- README
- add project description
- add run instructions
- add team contribution breakdown

Commit message:
- Wrote README with setup instructions and team contributions



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



