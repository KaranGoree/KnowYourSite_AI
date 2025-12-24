from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse

def crawl_website(base_url, max_pages=60):
    visited = set()
    to_visit = [base_url]
    texts = []

    domain = urlparse(base_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            res = requests.get(url, timeout=10)
            if "text/html" not in res.headers.get("Content-Type", ""):
                continue

            soup = BeautifulSoup(res.text, "html.parser")

            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)
            if len(text.split()) > 80:
                texts.append(text)

            visited.add(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(base_url, link["href"])
                parsed = urlparse(full_url)
                if parsed.netloc == domain and full_url not in visited:
                    to_visit.append(full_url)

        except:
            continue

    return texts
