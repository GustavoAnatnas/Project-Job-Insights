from functools import lru_cache
from typing import List, Dict
import csv

path = "data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


# print(read(path))


def get_unique_job_types(path: str) -> List[str]:
    file = read(path)
    job_types = []
    for job in file:
        if job["job_type"] not in job_types and job["job_type"] != "":
            job_types.append(job["job_type"])
    return job_types


# print(get_unique_job_types(path))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    filtered_jobs = []

    for job in jobs:
        if job_type == job["job_type"]:
            filtered_jobs.append(job)

    return filtered_jobs


# print(filter_by_job_type(read(path), "FULL_TIME"))
