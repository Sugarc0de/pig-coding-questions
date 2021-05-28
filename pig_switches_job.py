# Method: Simple Sorting
def longest_job_sequence(jobs):
    return list(sorted(jobs))


jobs = [(60, 6), (60, 7), (60, 4), (20, 3), (10, 1), (100, 8), (120, 5)]
# [(10, 1), (20, 3), (60, 4), (60, 6), (60, 7), (100, 8), (120, 5)]
print(longest_job_sequence(jobs))
