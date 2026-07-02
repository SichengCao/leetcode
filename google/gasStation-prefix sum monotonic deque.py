from collections import deque
def all_start_points(gas, cost):
    n = len(gas)

    # Step 1: diff
    diff = [gas[i] - cost[i] for i in range(n)]

    # Step 2: prefix (长度 2n + 1)
    prefix = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        prefix[i] = prefix[i - 1] + diff[(i - 1) % n]
    print("Prefix: ", prefix)
    res = []
    dq = deque()  # 单调递增队列（存 index）

    # Step 3: 初始化窗口 [1 ... n]
    for i in range(1, n + 1):
        while dq and prefix[dq[-1]] >= prefix[i]:
            dq.pop()
        dq.append(i)
    print("Init Queue: " , dq)
    # Step 4: 滑动窗口
    for start in range(n):
        # 判断当前 start 是否合法
        if prefix[dq[0]] >= prefix[start]:
            res.append(start)

        # 移除窗口左边界 (start+1)
        if dq and dq[0] == start + 1:
            dq.popleft()

        # 加入新元素 (start+n+1)
        nxt = start + n + 1
        while dq and prefix[dq[-1]] >= prefix[nxt]:
            dq.pop()
        dq.append(nxt)

    return res


def main():
    # 示例测试
    gas = [3, 3, 4, 3, 3, 4]
    cost = [4, 3, 3, 4, 3, 3]

    result = all_start_points(gas, cost)

    print("Gas: ", gas)
    print("Cost:", cost)
    print("Valid start indices:", result)


if __name__ == "__main__":
    main()