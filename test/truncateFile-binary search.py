from collections import defaultdict


def truncate(file,max_logs):
        file_count = defaultdict(int)
        for i in range(len(file)):
                file_count[file[i][0]] +=1
        print("file_count: ", file_count)
        count = list(file_count.values())
        print("count", count)

        def check(x):
                total = 0
                for c in count:
                        total += min(x,c)
                return total <= max_logs

        left = 0
        right = max(count)
        while left <= right:
                mid = (left+right)//2
                if check(mid):
                        left = mid+1
                else:
                        right = mid-1

        cutoff = right
        print(cutoff)
        execute_pool = defaultdict(int)
        res = []
        for name,log in file:
                execute_pool[name]+=1
                if execute_pool[name] <= cutoff:
                        res.append((name,log))

        leftover = max_logs - len(res)
        selection_pool = defaultdict(int)
        for name, log in file:

                selection_pool[name] += 1

                # 这条已经在第一轮加入了
                if selection_pool[name] <= cutoff:
                        continue

                # 第一轮没加入
                if leftover > 0:
                        res.append((name, log))
                        leftover -= 1

                if leftover == 0:
                        break
        return res





file = [["A","log1"],
        ["A","log2"],
        ["A","log3"],
        ["B","log1"],
        ["B","log2"],
        ["B","log3"],
        ["B","log4"],
        ["C","log1"],
        ["C","log2"],
        ["C","log3"],
        ["D","log1"],
        ["D","log2"]]

max_logs = 9

res = truncate(file,max_logs)
print(res)
