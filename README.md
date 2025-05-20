# Stealth PDF Scraper

A web scraping script designed to extract and download PDF files from JavaScript-heavy, bot-protected websites using Selenium and BeautifulSoup4 to mimic real browser behavior and bypass 403 errors.

---

## 🎯 Project Goals

This project demonstrates how to:

- ✅ Parse content from websites that are designed to **block automated bots**, such as by:
  - Returning **HTTP 403 Forbidden** errors on direct URL requests.
  - Loading content **dynamically via JavaScript**, making it unavailable to traditional scrapers.
- ✅ Use **Selenium** to render JavaScript and make the script behave like a real browser.
- ✅ Use **BeautifulSoup4** to parse dynamically rendered HTML.
- ✅ Download PDF files using **Requests** with custom headers like `User-Agent` and `Referer` to mimic browser-originating traffic.

---

## 🌐 Example Use Case: Court Docket Scraping

To demonstrate its effectiveness, this script extracts PDF documents from a court docket on the [Stretto](https://cases.stretto.com/) legal case management site.

📄 **Target page:**

> [TGI Fridays First Day Motions & Orders](https://cases.stretto.com/TGIFridays/court-docket/court-docket-category/2401-first-day-motions-orders/)

This page:
- Loads table content dynamically using JavaScript.
- Blocks direct PDF downloads by returning HTTP 403 for non-browser requests.
- Embeds document links inside `<tr class="document-name">` rows within a custom HTML table.

The script successfully:
- Renders the page using Selenium.
- Extracts all PDF URLs with BeautifulSoup.
- Downloads the files using `requests` with correct headers.

---

## 🛠 Tech Stack

- `Python 3`
- `Selenium` (headless Chrome)
- `BeautifulSoup4`
- `Requests`

---

## 🚀 Getting Started

Install dependencies:

```bash
pip install selenium beautifulsoup4 requests
