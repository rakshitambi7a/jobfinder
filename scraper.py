import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword = "python", location = "remote"):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch jobs")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    for row in soup.find_all('tr', class_='job'):
        title = row.find('h2')
        company = row.find('h3')
        if title and company:
            jobs.append({
                'title': title.get_text(strip=True),
                'company': company.get_text(strip=True),
                'location': location,
            })

    return jobs
