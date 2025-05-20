import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ------------------ Configuration ------------------ #

url = "https://cases.stretto.com/TGIFridays/court-docket/court-docket-category/2401-first-day-motions-orders/"
download_dir = "tgifridays_pdfs"
os.makedirs(download_dir, exist_ok=True)

# ------------------ Setup Selenium ------------------ #

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

# ------------------ Load and Wait for Table ------------------ #

driver.get(url)

# Step 1: Wait for table to load
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "custom-pleading-button-table"))
    )
except TimeoutException:
    driver.quit()
    raise Exception("Table with id 'custom-pleading-button-table' not found.")

# Step 2: Wait for rows to appear
max_wait = 20
waited = 0
rows = []

while waited < max_wait:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', id='custom-pleading-button-table')
    if table:
        rows = table.find_all('tr', class_='document-name')
        if rows:
            break
    time.sleep(1)
    waited += 1

driver.quit()

if not rows:
    raise Exception("Document rows not found in the table after waiting.")

# ------------------ Extract PDF Links ------------------ #

pdf_urls = []

for row in rows:
    td = row.find('td')
    if td:
        a_tag = td.find('a', href=True)
        if a_tag and a_tag['href'].endswith('.pdf'):
            full_url = urljoin(url, a_tag['href'])
            pdf_urls.append(full_url)

# ------------------ Download PDFs ------------------ #

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Referer': url,
}

for pdf_url in pdf_urls:
    file_name = os.path.basename(pdf_url)  # use filename from URL
    file_path = os.path.join(download_dir, file_name)
    print(f"Downloading: {pdf_url} -> {file_path}")
    try:
        response = requests.get(pdf_url, headers=headers, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {pdf_url}: {e}")
