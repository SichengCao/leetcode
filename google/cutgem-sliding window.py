from collections import defaultdict

def split_three_types(gems):
    n = len(gems)
    if n % 2 != 0:
        return False  # 必须能平分

    h = n // 2  # window size

    # 1️⃣ 统计总数
    total = defaultdict(int)
    for g in gems:

        total[g] += 1
    print("total")
    print(total)
    # 2️⃣ 检查是否可平分
    target = {}
    for g in total:
        if total[g] % 2 != 0:
            return False
        target[g] = total[g] // 2
    print("target")
    print(target)

    # 3️⃣ 初始化窗口 [0 ... h-1]
    window = defaultdict(int)
    print("window")
    for i in range(h):
        window[gems[i]] += 1

    print(window)

    # 判断函数
    def is_valid():
        for g in target:
            if window[g] != target[g]:
                return False
        return True

    # 情况1：前半段
    if is_valid():
        return True

    # 4️⃣ 滑动窗口
    for i in range(n - h):
        # 移出左边
        left = gems[i]
        window[left] -= 1

        # 加入右边
        right = gems[i + h]
        window[right] += 1

        if is_valid():
            return True

    return False


gems = ['A','B','C','A','B','C']
split_three_types(gems)