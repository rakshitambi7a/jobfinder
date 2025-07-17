import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword="python", location="India", max_pages=1, minimum_stipend="10000"):
    url = f"https://internshala.com/internships/{keyword.replace(' ', '-')}-internship/stipend-{minimum_stipend}/"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("❌ Failed to fetch jobs from Internshala.")
        return []

    soup = BeautifulSoup(res.text, 'html.parser')
    cards = soup.find_all('div', class_='internship_meta')

    if not cards:
        print("❌ No internships found.")
        return []

    job_data = []

    for card in cards:
        parent = card.find_parent('div', class_='individual_internship')
        title_elem = parent.find('a', id='job_title')
        company_elem = parent.find('p', class_='company-name')
        location_elem = parent.find('div', class_='locations')
        posted_date_div = parent.find('div', class_='status-info')
        posted_date_elem = posted_date_div.find('span') if posted_date_div else None
        
        stipend_elem = parent.find('span', class_='stipend')

        job_data.append({
            "title": title_elem.get_text(strip=True) if title_elem else "N/A",
            "company": company_elem.get_text(strip=True) if company_elem else "N/A",
            "location": location_elem.get_text(strip=True) if location_elem else "N/A",
            "posted_date": posted_date_elem.get_text(strip=True) if posted_date_elem else "N/A",
            "stipend": stipend_elem.get_text(strip=True) if stipend_elem else "N/A",
        })

    return job_data
