import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# List of usernames to scrape
usernames_list =[['USERNAME', 'USERNAME'], ['USERNAME', 'USERNAME']]
# Set Up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# To run without opening a browser window, uncomment the following line:
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Initialize an empty DataFrame to store all data
all_data = []

# Counter for consecutive errors (any error type)
consecutive_errors = 0
max_consecutive_errors = 5

# Loop through each username list
for i, usernames in enumerate(usernames_list):
    print(f"Starting to scrape list {i+1} with {len(usernames)} usernames.")

    # List to store results for this batch
    data = []

    for username in usernames:
        try:
            # Open the profile page
            driver.get(f'https://x.com/{username}')
            driver.implicitly_wait(5)  # Wait for elements to load

            # Locate the follower count using XPath
            follower_count_element = driver.find_element(By.XPATH, '//a[contains(@href,"followers")]/span[1]/span[1]')
            follower_count = follower_count_element.text

            print(f'{username} has {follower_count} followers.')
            data.append([username, follower_count])

            # Reset the error counter after a successful retrieval.
            consecutive_errors = 0

        except Exception as e:
            print(f"Could not retrieve follower count for {username}: {e}")
            data.append([username, "Error"])

            # Increment the counter for every error regardless of its type.
            consecutive_errors += 1

            # If we've hit the error threshold, break the loop.
            if consecutive_errors >= max_consecutive_errors:
                print(f"Encountered {max_consecutive_errors} consecutive errors. Stopping the run for this batch.")
                break

    # Add this batch's data to the overall data list
    all_data.extend(data)

    # Save results to Excel after each list (you can adjust file naming as needed)
    df = pd.DataFrame(data, columns=["Username", "Follower Count"])
    df.to_excel(f"scraper_results_batch_{i+1}.xlsx", index=False)

    print(f"Finished scraping list {i+1}. Data saved to 'scraper_results_batch_{i+1}.xlsx'.")

    # Optional: Restart the browser every batch or after certain intervals
    driver.quit()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Close the browser after the last batch is done
driver.quit()

# Combine all data into a final DataFrame
final_df = pd.DataFrame(all_data, columns=["Username", "Follower Count"])

# Save the final DataFrame to an Excel file
final_df.to_excel("final_scraper_results.xlsx", index=False)

print("Scraping completed for all lists. Final data saved to 'final_scraper_results.xlsx'.")
