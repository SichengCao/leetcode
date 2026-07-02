from collections import defaultdict

def split_k_types_fast(gems):
    n = len(gems)
    if n % 2 != 0:
        return False

    h = n // 2

    # 统计总数
    total = defaultdict(int)
    for g in gems:
        total[g] += 1

    # 构造 target
    target = {}
    for g in total:
        if total[g] % 2 != 0:
            return False
        target[g] = total[g] // 2


    print("target", target)

    # print("target")
    # print(target)

    need = len(target)  # 需要匹配的种类数
    # print("need")
    # print(need)

    # 初始化 window
    window = defaultdict(int)
    for i in range(h):
        window[gems[i]] += 1

    print("Window", window)
    # 初始化 match
    match = 0
    for g in target:
        if window[g] == target[g]:
            match += 1
    print("match", match)
    print("need",need)

    if match == need:
        return True


    # 滑动窗口
    for i in range(n - h):
        left = gems[i]
        right = gems[i + h]

        # ❗处理 left（移出）
        if window[left] == target[left]:
            match -= 1
        window[left] -= 1
        if window[left] == target[left]:
            match += 1

        # ❗处理 right（加入）
        if window[right] == target[right]:
            match -= 1
        window[right] += 1
        if window[right] == target[right]:
            match += 1

        if match == need:
            return True
   

    return False

gems = ['A','B','C','B','A','B','C','C','A','A','B','C']
split_k_types_fast(gems)