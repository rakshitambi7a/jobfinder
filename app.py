import streamlit as st
from scraper import scrape_jobs
from filter import filter_jobs
import pandas as pd

st.title("🧠 JobFinder")
st.write("Scrapes remote jobs and ranks them by your keywords.")

keyword = st.text_input("Job keyword (e.g., python)", "python")
location = st.text_input("Location", "remote")
filters = st.text_input("Ranking keywords (comma-separated)", "intern,developer,junior")

if st.button("Find Jobs"):
    jobs = scrape_jobs(keyword, location)
    filter_keywords = [k.strip() for k in filters.split(',')]
    ranked = filter_jobs(jobs, filter_keywords)
    st.success(f"Found {len(ranked)} jobs!")
    st.dataframe(ranked)
    st.download_button("Download CSV", ranked.to_csv(index=False), "jobs.csv", "text/csv")
