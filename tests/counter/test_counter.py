from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "analyst") == 1100
    assert count_ocurrences("data/jobs.csv", "engineer") == 5017
