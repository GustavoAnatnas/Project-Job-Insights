from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    industries = []
    for job in file:
        if job["industry"] not in industries and job["industry"] != "":
            industries.append(job["industry"])
    return industries


# print(get_unique_industries("data/jobs.csv"))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    filtered_jobs_by_industry = []

    for job in jobs:
        if industry == job["industry"]:
            filtered_jobs_by_industry.append(job)

    return filtered_jobs_by_industry


# print(filter_by_industry(read("data/jobs.csv"), "Finance"))
