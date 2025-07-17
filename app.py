import streamlit as st
from scraper import scrape_jobs
from filter import filter_jobs
import pandas as pd

st.set_page_config(page_title="JobFinder India", layout="centered")
st.title("🇮🇳 JobFinder: Intern Roles in India")
st.caption("Scrapes current job listings from Indeed India and ranks them based on your filters.")

with st.form("job_search_form"):
    keyword = st.text_input("Job Title / Keyword", value="python intern")
    location = st.text_input("Location", value="India")
    filters = st.text_input("Ranking Keywords (comma-separated)", value="intern, developer, junior")
    minimum_stipend = st.text_input("Minimum Stipend", value="10000")
    pages = st.slider("Pages to Scrape", 1, 3, 1)
    submitted = st.form_submit_button("Find Jobs")

if submitted:
    with st.spinner("🔍 Searching Indeed India..."):
        try:
            jobs = scrape_jobs(keyword, location, max_pages=pages, minimum_stipend=minimum_stipend)
            if not jobs:
                st.warning("No jobs found. Try changing the keyword or location.")
            else:
                filter_keywords = [k.strip() for k in filters.split(",")]
                ranked_jobs = filter_jobs(jobs, filter_keywords)

                st.success(f"Found {len(ranked_jobs)} jobs!")
                st.dataframe(ranked_jobs)

                csv = ranked_jobs.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ Download CSV", data=csv, file_name="jobs.csv", mime="text/csv")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
