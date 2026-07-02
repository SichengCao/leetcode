def find_component(arr, diff, queries):

    n = len(arr)

    component = [0] * n

    comp_id = 0

    for i in range(1, n):

        # 出现断层
        if arr[i] - arr[i - 1] > diff:
            comp_id += 1

        component[i] = comp_id

    ans = []

    for u, v in queries:
        ans.append(component[u] == component[v])

    return ans


def nodeConnectivity(arr, diff, queries):

    n = len(arr)
    ranges = []

    start = 0

    for i in range(1, n):
        # gap found -> new component
        if arr[i] - arr[i - 1] > diff:
            ranges.append([start, i - 1])
            start = i

    ranges.append([start, n - 1])

    print("Connected Components (Ranges):")
    print(ranges)
    print()

    # -----------------------------------
    # Binary Search:
    # find which range contains target
    # -----------------------------------

    def find_range(target):

        left = 0
        right = len(ranges) - 1

        while left <= right:

            mid = (left + right) // 2

            start, end = ranges[mid]

            print(
                f"Searching target={target}, "
                f"checking range={ranges[mid]}"
            )

            # target inside this range
            if start <= target <= end:
                return mid

            # go left
            elif target < start:
                right = mid - 1

            # go right
            else:
                left = mid + 1

        return -1

    # -----------------------------------
    # Process queries
    # -----------------------------------

    result = []

    for u, v in queries:

        print(f"\nQuery: [{u}, {v}]")

        range_u = find_range(u)
        range_v = find_range(v)

        print(f"u belongs to component {range_u}")
        print(f"v belongs to component {range_v}")

        connected = (range_u == range_v)

        print(f"Connected? {connected}")

        result.append(connected)

    return result


# -----------------------------------
# Main
# -----------------------------------

def main():

    arr = [1, 2, 3, 10, 11, 20]

    diff = 2

    queries = [
        [0, 2],   # True
        [1, 4],   # False
        [3, 4],   # True
        [0, 5]    # False
    ]

    ans = nodeConnectivity(arr, diff, queries)

    print("\nFinal Answer:")
    print(ans)


main()



arr = [1,2,3,10,11]
diff = 2

print(nodeConnectivity(arr,diff,[[1,2],[2,4]]))

# print(find_component(arr,diff,[[1,2],[2,3]]))