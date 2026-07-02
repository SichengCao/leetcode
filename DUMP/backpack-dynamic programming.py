def correct_knapsack():
    W = 4
    items = [("A", 2, 10), ("B", 2, 10)]

    dp = [0] * (W + 1)

    print("\n=== 正确写法（物品在外 + 倒序）===")

    for name, w, v in items:
        print(f"\n=== 处理物品 {name} ===")
        for j in range(W, w - 1, -1):
            before = dp[j]
            dp[j] = max(dp[j], dp[j - w] + v)

            print(f"dp[{j}] = max({before}, dp[{j - w}] + {v})")
            print(f"当前 dp: {dp}")

    print("\n最终 dp:", dp)


def wrong_knapsack():
    W = 4
    items = [("A", 2, 10), ("B", 2, 10)]

    dp = [0] * (W + 1)

    print("=== 错误写法（容量在外）===")

    for j in range(W + 1):
        print(f"\n--- 容量 j = {j} ---")
        for name, w, v in items:
            if j >= w:
                before = dp[j]
                dp[j] = max(dp[j], dp[j - w] + v)

                print(f"用物品 {name}: dp[{j}] = max({before}, dp[{j - w}] + {v})")
                print(f"当前 dp: {dp}")

    print("\n最终 dp:", dp)

wrong_knapsack()
# correct_knapsack()