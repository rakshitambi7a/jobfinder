from scraper import scrape_jobs
from filter import filter_jobs
import json

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    keyword = config.get("keyword", "python")
    location = config.get("location", "remote")
    filter_keywords = config.get("filters", ["intern", "developer"])

    jobs = scrape_jobs(keyword, location)
    ranked_jobs = filter_jobs(jobs, filter_keywords)

    print(ranked_jobs.head(10))
    ranked_jobs.to_csv("output.csv", index=False)
