# Wuzzuf Job Scraper

A Python script to scrape job listings from Wuzzuf.net based on user input (e.g., data science, machine learning), and save results as CSV files.

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- pandas

Install using:

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the script:
   ```bash
   python your_script_name.py
   ```

2. When prompted, enter job titles separated by commas, for example:
   ```
   data science, machine learning
   ```

3. CSV files will be saved in the current directory as follows: 
    ```
    data_science.csv
    machine_learning.csv
    ```

### with columns:
- link
- title
- company
- location
- specs

## Notes

- This script adds a short delay between requests to avoid being blocked.
- For educational use only. Do not use for large-scale scraping or commercial purposes.
