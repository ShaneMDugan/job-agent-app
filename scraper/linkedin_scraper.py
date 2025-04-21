import requests
from bs4 import BeautifulSoup

def get_jobs_from_linkedin(keyword="Product Owner", location="Remote", max_results=5):
    query = keyword.replace(" ", "%20")
    url = f"https://www.linkedin.com/jobs/search?keywords={query}&location={location}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    links = []
    for job_tag in soup.find_all("a", class_="base-card__full-link")[:max_results]:
        links.append(job_tag['href'])

    return links
