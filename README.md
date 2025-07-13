# Traffic Analysis Coursework

This is a Python project developed as part of the Software Development I module. The application analyses collected traffic flow data to generate insights and visualizations.

---

## Features

- User input validation for date selection (DD MM YYYY format)
- CSV file selection based on user data
- Analysis of vehicle data including:
  - Total vehicles, trucks, and electric vehicles
  - Speed violations
  - Two-wheeled vehicles
  - Peak traffic hours
  - Scooter percentage
  - Bicycles per hour
- Results displayed in the terminal and saved to 'results.txt'
- Class-based GUI histogram using 'tkinter'
- Option to process multiple datasets in one run

---

## Technologies Used

- Python 3.12
- CSV parsing
- File handling
- Data processing with lists and conditions
- Tkinter for histogram and GUI drawing

---

## Files

| File                           | Description                            |
|--------------------------------|----------------------------------------|
| `traffic_analysis.py`          | Main Python program                    |
| `results.txt`                  | Text file containing analysis results  |
| `traffic_data_15_05_2015.csv`  | Sample input datasets for testing      |
| `traffic_data_15_06_2024.csv`  | Sample input datasets for testing      |
| `traffic_data_16_06_2024.csv`  | Sample input datasets for testing      |
| `traffic_data_21_06_2024.csv`  | Sample input datasets for testing      |

---

## How to Run

1. Open `traffic_analysis.py` in IDLE or your preferred IDE.
2. Run the script.
3. Enter the survey date (DD MM YYYY) when prompted.
4. The program will:
     - Analyse the selected CSV
     - Show results in the terminal
     - Save them in `results.txt`
     - Display a histogram using Tkinter
  
---

## Coursework Details

- Module: 4COSC006C – Software Development I
- Academic Year: 2024/25
- Institution: Informatics Institute of Technology (IIT), Sri Lanka
- Degree: BSc (Hons) Computer Science – Awarded by the University of Westminster
