from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    max_salary = []
    for job in file:
        if job["max_salary"].isdigit():
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


# print(get_max_salary("data/jobs.csv"))


def get_min_salary(path: str) -> int:
    file = read(path)
    min_salary = []
    for job in file:
        if job["min_salary"].isdigit():
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


# print(get_min_salary("data/jobs.csv"))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        salary = int(salary)
    except (TypeError, KeyError):
        raise ValueError("Invalid job or salary")
    if min > max:
        raise ValueError("min_salary is greather than max_salary")
    return salary >= min and salary <= max


# print(matches_salary_range({"min_salary": 1000, "max_salary": 2000}, 1500))


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return filtered_jobs_by_salary_range
