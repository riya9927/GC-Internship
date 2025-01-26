from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()  

query = "internshala"

driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

time.sleep(2)

results = []
search_results = driver.find_elements(By.CLASS_NAME, "tF2Cxc")
for result in search_results:
    title = result.find_element(By.TAG_NAME, "h3").text
    url = result.find_element(By.TAG_NAME, "a").get_attribute("href")
    description = result.find_element(By.CLASS_NAME, "VwiC3b").text
    results.append({"Title": title, "URL": url, "Description": description})

df = pd.DataFrame(results)
df.to_csv("google_search_results.csv", index=False)

driver.quit()

print("Scraping completed. Results saved to google_search_results.csv.")
