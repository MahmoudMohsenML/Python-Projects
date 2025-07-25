import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Base URL for Wuzzuf job search
base_url = "https://wuzzuf.net/search/jobs/?q={}&a=hpb&start={}"
jobs = []  # List to hold extracted job data

# user input its desired job titles, separated by commas
print("Enter jobs to scrape their data, enter your input in this form--> data science,machine learning,...etc")
try:
    user_input_jobs = input()
    jobs_list = user_input_jobs.split(",")  # Split input by commas
    cleaned_jobs = [
        job.strip().replace(" ", "%20") 
        for job in jobs_list 
        if job.strip()
    ]  # Clean spaces and URL-encode spaces

    if not cleaned_jobs:
        print("No valid job titles.")

except ValueError as ve:
    print(f"Input Error: {ve}")
    cleaned_jobs = []

except AttributeError as ae:
    print(f"String operation failed: {ae}")
    cleaned_jobs = []

# Iterate over each cleaned job title entered by the user
for job_title in cleaned_jobs:
    page = 0  # Start from the first page
    while True:
        url = base_url.format(job_title, page)  # Format URL with job title and current page
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all job cards on the page using the div class  
        job_cards = soup.find_all("div", class_="css-1gatmva e1v1l3u10")

        # If no jobs are found, break the While loop 
        if not job_cards:
            print("pages ended.")
            break

        # Extract relevant job details from each job card
        for job in job_cards:
            link = job.find("a", class_="css-o171kl")
            title = job.find("a", class_="css-o171kl")
            company = job.find("a", class_="css-17s97q8")
            location = job.find("span", class_="css-5wys0k")
            specs = job.find("div", class_="css-y4udm8")

            job_details = {
                "link": link.get("href") if link else "NaN",
                "title": title.text if title else "NaN",
                "company": company.text if company else "NaN",
                "location": location.text if location else "NaN",
                "specs": specs.text if specs else "NaN"
            }
            
            jobs.append(job_details)

        page += 1  # Move to the next page
        time.sleep(1)  # delay to avoid Blocking

    # Save the scraped job data to a CSV file for each job title
    df = pd.DataFrame(jobs)
    df.to_csv(f"{job_title.replace('%20', '_')}.csv", index=False)
    jobs = []  # Reset the jobs list before processing the next title

print(f"{len(cleaned_jobs)} CSV file(s) created.")
