from collections import defaultdict


def cutgem_K_types(gems):
    n = len(gems)
    if n % 2 != 0 :
        return False
    h = n // 2
    gem_count = defaultdict(int)
    for gem in gems:
        gem_count[gem]+=1


    match = dict()
    for gem, count in gem_count.items():
        if count % 2 != 0:
            return False
        match[gem] = count // 2

    window = defaultdict(int)
    for i in range(h):
        window[gems[i]]+=1
    if window == match:
        return True

    for start in range(n-h):
        window[gems[start]]-=1
        if window[gems[start]] == 0:
            del window[gems[start]]
        window[gems[start+h]]+=1
        if window == match:
            return True
    return False

def cutgem_K_types_1(gems):
    n = len(gems)
    if n % 2 != 0 :
        return False
    h = n // 2
    gem_count = defaultdict(int)
    for gem in gems:
        gem_count[gem]+=1


    match = dict()
    for gem, count in gem_count.items():
        if count % 2 != 0:
            return False
        match[gem] = count // 2

    window = defaultdict(int)
    for i in range(h):
        window[gems[i]]+=1

    matched = 0
    for gem in match:
        if window.get(gem,0) == match[gem]:
            matched += 1
    if matched == len(match):
        return True

    for start in range(n-h):
        left = gems[start]
        if window[left] == match[left]:
            matched -= 1
        window[left] -= 1

        if window[left] == match[left]:
            matched+=1
        if window[left] == 0:
            del window[left]

        right = gems[start + h]

        # 更新前如果已经匹配，先取消
        if window.get(right, 0) == match[right]:
            matched -= 1

        window[right] += 1

        # 更新后如果重新匹配，再恢复
        if window[right] == match[right]:
            matched += 1


if __name__ == "__main__":

    tests = [
        ['A', 'B', 'C', 'A', 'B', 'C'],           # True（一刀）
        ['A', 'A', 'B', 'C', 'B', 'C'],           # True（两刀）
        ['A', 'B', 'A', 'B', 'C', 'C'],           # True
        ['A', 'A', 'A', 'B', 'B', 'B'],           # False
        ['A', 'B', 'C', 'A', 'A', 'C'],           # False（A=3）
        ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'], # True（四种）
    ]

    for gems in tests:
        print("-" * 40)
        print("Input :", gems)
        print("Result:", cutgem_K_types(gems))