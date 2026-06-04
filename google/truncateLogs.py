from collections import defaultdict


def truncate_logs(messages, max_logs):

    # -----------------------------------------
    # Step 1:
    # Count logs per source
    # -----------------------------------------
    count = defaultdict(int)

    for source, msg in messages:
        count[source] += 1

    counts = list(count.values())

    print(counts)

    # -----------------------------------------
    # Step 2:
    # Binary search maximum valid X
    # -----------------------------------------
    left = 0
    right = max(counts)

    def valid(x):

        total = 0

        for c in counts:
            total += min(c, x)

        return total <= max_logs

    ans = 0

    while left < right:

        mid = (left + right) // 2

        if valid(mid):

            # try larger X
            left = mid + 1

        else:

            right = mid

    X = left

    print("Best cutoff X =", X)

    # -----------------------------------------
    # Step 3:
    # Actually truncate
    # -----------------------------------------
    used = defaultdict(int)

    result = []

    for source, msg in messages:

        if used[source] < X:

            result.append((source, msg))

            used[source] += 1

    return result


# ------------------------------------------------
# MAIN
# ------------------------------------------------

def main():

    messages = [

        ("A", "log1"),
        ("A", "log2"),
        ("A", "log3"),
        ("A", "log4"),
        ("A", "log5"),

        ("B", "log1"),
        ("B", "log2"),

        ("C", "log1"),
        ("C", "log2"),
        ("C", "log3"),
        ("C", "log4"),

        ("D", "log1")
    ]

    max_logs = 8

    result = truncate_logs(messages, max_logs)

    print("\nFinal logs:\n")

    for source, msg in result:
        print(source, msg)


main()