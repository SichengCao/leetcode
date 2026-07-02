def split_two_gems(gems):
    n = len(gems)
    if n % 2 !=0:
        return False
    h = n//2
    totalD = gems.count('D')
    totalR = n - totalD

    if totalD % 2 != 0 or totalR % 2 != 0:
        return False
    targetD = totalD//2
    targetR = totalR//2

    cntD = 0
    cntR = 0

    for i in range(h):
        if gems[i] == 'D':
            cntD += 1
        else:
            cntR += 1

    if cntD == targetD and cntR == targetR:
        print("C1: ", gems[0:h])
        print("C2: ", gems[h:])
        return True

    for i in range(n-h):
         if gems[i] == 'D':
            cntD -=1
         else:
             cntR-=1

         if gems[i+h] == 'D':
             cntD += 1
         else:
             cntR += 1

         if cntD == targetD and cntR == targetR:
             print("C1: ", gems[i+1:i + h+1])
             print("C2: ", gems[0:i+1]+gems[i+h+1:])

             return True
    return False



if __name__ == "__main__":

    gems1 = ['D', 'R', 'D', 'R']
    print(split_two_gems(gems1))   # True

    gems2 = ['D', 'D', 'R', 'R']
    print(split_two_gems(gems2))   # True

    gems3 = ['D', 'D', 'D', 'R']
    print(split_two_gems(gems3))   # False（D 无法平分）

    gems4 = ['D', 'R', 'R', 'D', 'D', 'R']
    print(split_two_gems(gems4))   # True

    gems5 = ['D', 'D', 'R', 'D', 'R', 'R']
    print(split_two_gems(gems5))   # True 或 False（可以自己验证）


