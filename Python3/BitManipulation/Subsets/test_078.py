from Binary078 import Solution as binary
from DFS078 import Solution as dfs
from Backtracking078 import Solution as backtracking
from Naive078 import Solution as naive

testcase = []
testcase.append([1, 2, 3])
testcase.append([])

answer = []
answer.append([
    [3],
    [1],
    [2],
    [1, 2, 3],
    [1, 3],
    [2, 3],
    [1, 2],
    []
])
answer.append([[]])


def test_binary():
    for i, case in enumerate(testcase):
        assert sorted(binary().subsets(case)) == sorted(answer[i])


def test_dfs():
    for i, case in enumerate(testcase):
        assert sorted(dfs().subsets(case)) == sorted(answer[i])


def test_backtracking():
    for i, case in enumerate(testcase):
        assert sorted(backtracking().subsets(case)) == sorted(answer[i])


def test_naive():
    for i, case in enumerate(testcase):
        assert sorted(naive().subsets(case)) == sorted(answer[i])
