# Data Scraping and Standardization Project

## Overview

This project aims to scrape data related to construction and infrastructure projects in California from various sources, standardize the data, and automate the entire process.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, `pandas`, `tqdm`, `spacy`

### Installation

1. **Clone the repository or download the scripts**:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install the required libraries**:
   ```sh
   pip install requests beautifulsoup4 pandas tqdm spacy
   python -m spacy download en_core_web_sm
   ```

### Running the Scripts

1. **Run the scraper script**:
   ```sh
   python scraper.py
   ```

2. **Run the standardization script**:
   ```sh
   python standardize.py
   ```

3. **Run the automation script**:
   ```sh
   python automate.py
   ```

### Automated Execution

#### On Unix-like Systems

1. **Create a shell script (`run_automation.sh`)**:
   ```sh
   #!/bin/bash
   python3 /path/to/automate.py
   ```
   Make the script executable:
   ```sh
   chmod +x run_automation.sh
   ```

2. **Set up a cron job**:
   ```sh
   crontab -e
   ```
   Add the following line to run the script daily at midnight:
   ```sh
   0 0 * * * /path/to/run_automation.sh
   ```

#### On Windows

1. **Create a batch file (`run_automation.bat`)**:
   ```bat
   @echo off
   python "C:\path\to\automate.py"
   ```

2. **Schedule a task using Task Scheduler**:
   - Open Task Scheduler and create a new task.
   - Set the trigger to run daily at your preferred time.
   - Set the action to start the batch file you created.

## Sample Datasets

- **Raw Data**: `raw_data.csv` 
- **Standardized Data**: `standardized_data.csv` 
