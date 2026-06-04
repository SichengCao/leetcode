from collections import defaultdict, deque


def pickSequence(points, sticks, n):

    indegree = [0] * n
    pickMap = defaultdict(list)
    for pre, curr in sticks:
        indegree[curr] += 1
        pickMap[pre].append(curr)
    print(pickMap)
    print(indegree)

    res = 0
    queue = deque()

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        res += points[curr]

        for stick in pickMap[curr]:
            indegree[stick] -= 1
            if indegree[stick] == 0:
                queue.append(stick)



    return res





n = 4

points = [5, 10, 20, 15]

sticks = [
    (0, 1),
    (1, 2),
    (3, 2)
]

output = pickSequence(points,sticks,n)
print(output)