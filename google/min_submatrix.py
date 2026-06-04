def min_submatrix(matrix, k):
    n = len(matrix)
    m = len(matrix[0])

    # 1️⃣ 构建 prefix
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    print(prefix)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (
                matrix[i-1][j-1]
                + prefix[i-1][j]
                + prefix[i][j-1]
                - prefix[i-1][j-1]
            )

    print(prefix)

    # 2️⃣ 枚举 k×k
    min_sum = float('inf')

    for i in range(n - k + 1):
        for j in range(m - k + 1):

            curr_sum = (
                prefix[i+k][j+k]
                - prefix[i][j+k]
                - prefix[i+k][j]
                + prefix[i][j]
            )

            min_sum = min(min_sum, curr_sum)

    return min_sum


# ✅ main 函数
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    k = 2

    result = min_submatrix(matrix, k)
    print("Minimum k x k submatrix sum:", result)