import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# List of usernames to scrape
usernames = [
 'scherfcom', 'prince3833', 'SYNDICATE369', '333blacksea', 'PippinCrazee', 'Srosh_Mayi', 'ArcaneusLord', 'x46gill', 'fugasok',
 'LeonidasPanagi2', '9Muratayhan', 'wallstreetgibs', 'esoteric_jayz', 'DipFinding', 'el2222_H', 'JulyAeternum', 'Crypto_Xleaks', 'CryptonianZee', 'grvcapital22', 'PnFChart1986', 'crypthal', 'rditrych', 'low_cap41279', 'waldalhas1',
 'artimemes', 'StanleyCrypto_1', 'sensei_kong', 'TradingTarzan', 'CelaEndrit', 'BuffaloNYMonkey', 'P_Charlie_88', 'MemeseusMaximus', 'riskreaper001', 'goel_siddharth', 'ErickEliot18', '5TONEOFFICIAL', 'DhandhaPaani', 'That_sHowUFeel', 'milko52250068',
 'bokemtrader', 'Soran989', 'ChiTown_A', 'ChartTarangul', 'AlmuhandesKSA', 'MPBHH', 'OmarAlkhazraji6', 'P85Crypto', 'AeonOrmu', 'Jus_Trades', 'BATM017', 'RicardoVidal899', 'TrendsharksLive', 'AhoNiranjana'
]


# Set Up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# To run without opening a browser window, uncomment the following line:
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# List to store results
data = []

# Counter for consecutive errors (any error type)
consecutive_errors = 0
max_consecutive_errors = 5

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
            print(f"Encountered {max_consecutive_errors} consecutive errors. Stopping the run.")
            break

# Close the browser
driver.quit()

# Save data to an Excel file
df = pd.DataFrame(data, columns=["Username", "Follower Count"])
df.to_excel("C:/Users/sgj/OneDrive - Alfotech/Skrivebord/scraperfolder/x_follower_counts48.xlsx", index=False)

print("Scraping completed.")
