## Project Goals

This project demonstrates how to:

- Parse content from websites that are designed to **block automated bots**, such as by:
  - Returning **HTTP 403 Forbidden** errors on direct requests.
  - Loading actual content (like PDFs or tables) **dynamically via JavaScript**.
- Use **Selenium** to render JavaScript and make the script behave like a real user/browser.
- Use **BeautifulSoup4** to parse rendered HTML content.
- Download PDF files with custom headers (e.g., `User-Agent`, `Referer`) to bypass access restrictions.

This pattern is commonly required for:
- Legal document repositories
- Court docket archives
- Government websites
- Financial or compliance documents


### Tech Stack
- `Python 3`
- `Selenium` (headless Chrome)
- `BeautifulSoup4`
- `Requests` with custom headers