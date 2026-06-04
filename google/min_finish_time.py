import heapq

def can_finish(start_times, S, C, T):
    heap = [0] * C  # CPU available time
    heapq.heapify(heap)

    for t in start_times:
        cpu_free = heapq.heappop(heap)

        start = max(t, cpu_free)
        end = start + S

        if end > T:
            return False

        heapq.heappush(heap, end)

    return True


def min_finish_time(start_times, S, C):
    start_times.sort()

    left = min(start_times)
    right = max(start_times) + len(start_times) * S

    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_finish(start_times, S, C, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans