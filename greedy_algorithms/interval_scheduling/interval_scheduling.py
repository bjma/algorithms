# Define jobs as an object with a start time and finish time
class Job:
    def __init__(self, s=0, f=0):
        self.s = s
        self.f = f

# Init list of jobs; using example from greedy_algorithms.md
jobs = [Job(0, 0), Job(0, 6), Job(1, 4), Job(3, 5), Job(3, 8), 
        Job(4, 7), Job(5, 9), Job(6, 10), Job(8, 11)]

# Let jobs be a list of jobs
# Let n be the number of jobs
def interval_scheduling(n, jobs):
    # sort finish times in increasing order
    jobs = sort_jobs(jobs)
    # list of selected jobs
    S = []

    for j in range(1, n):
        # if job j is compatible with the selected jobs
        if is_compatible(jobs[j], S):
            S.append(jobs[j])
    return S

# Returns a new list of jobs sorted by finish time in increasing order
# I'm using selection sort, but we can also use merge sort
def sort_jobs(jobs):
    n = len(jobs)
    for i in range(1, n):
        # min index
        k = i
        for j in range(i + 1, n):
            if jobs[k].f > jobs[j].f:
                k = j
        jobs[i], jobs[k] = jobs[k], jobs[i]
    return jobs

# Returns true if job is compatible with a list of jobs
def is_compatible(job, jobs):
    n = len(jobs)
    # base case
    if not jobs:
        return True
    # check for incompatibility
    # since jobs is sorted in increasing order of finish time,
    # simply checking if job.s is less than the min. finsih time
    # suffices, since jobs[0].f < jobs[1].f < ... < jobs[n].f
    return job.s < min_finish(jobs)

# Gets the minimum finish time in a list of jobs
# I'm doing this so we can check compatibility in O(n) time
# All this would be O(1) if we used two lists for s and f
def min_finish(jobs):
    n = len(jobs)
    # create list of finish times
    f = [jobs[j].f for j in range(1, n)]
    # return earliest finish time
    return min(f)