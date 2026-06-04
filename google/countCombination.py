#inclusion-exclusion
def countCombinations(N, user, bypass, t):
    range_size = 2 * t + 1

    # edge case
    if range_size >= N:
        return N ** 3

    def overlap(a, b):
        dist = abs(a - b)
        dist = min(dist, N - dist)
        return max(0, range_size - dist)

    overlap_total = 1
    for i in range(3):
        overlap_total *= overlap(user[i], bypass[i])

    return 2 * (range_size ** 3) - overlap_total


N = 10
t = 2

user   = [0, 1, 2]
bypass = [3, 4, 5]

print(countCombinations(N, user, bypass, t))