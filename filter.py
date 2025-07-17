import pandas as pd

def filter_jobs(jobs, keyword_list):
    df = pd.DataFrame(jobs)
    df['rank'] = df['title'].apply(
        lambda x: sum(1 for k in keyword_list if k.lower() in x.lower())
    )
    df = df.sort_values(by='rank', ascending=False)
    return df
