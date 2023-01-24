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


print(get_unique_job_types(path))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
