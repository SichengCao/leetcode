from collections import defaultdict

class Solution:
    def countPrefixPaths(self, n, edges, labels, s):
        # =========================
        # 1️⃣ 建图（邻接表）
        # =========================
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # res[i] 表示：匹配 s 的前 i+1 个字符的路径数量
        res = [0] * len(s)

        # =========================
        # 2️⃣ DFS
        # =========================
        def dfs(current_node, parent_node, current_path):
            """
            current_node: 当前在哪个节点
            parent_node: 上一个节点是谁（防止走回头路）
            current_path: 当前路径拼出来的字符串
            """

            # 把当前节点的字符加进路径
            current_path = current_path + labels[current_node]

            print(f"当前节点: {current_node}, path: '{current_path}'")

            # =========================
            # 剪枝1：长度超过 s，没必要继续
            # =========================
            if len(current_path) > len(s):
                print("  超过长度，返回")
                return

            # =========================
            # 判断是不是 s 的前缀
            # =========================
            prefix = s[:len(current_path)]

            if current_path == prefix:
                # 匹配成功
                res[len(current_path) - 1] += 1
                print(f"  匹配前缀 '{prefix}'，res = {res}")
            else:
                # 不匹配，直接停止这条路径
                print(f"  不匹配 '{prefix}'，剪枝返回")
                return

            # =========================
            # 继续往下走（所有邻居）
            # =========================
            for neighbor in graph[current_node]:
                # 防止走回头路
                if neighbor != parent_node:
                    dfs(neighbor, current_node, current_path)

        # =========================
        # 3️⃣ 每个节点作为起点
        # =========================
        for start in range(n):
            print(f"\n=== 从节点 {start} 开始 DFS ===")
            dfs(start, -1, "")

        return res


# =========================
# 🚀 主函数入口
# =========================
if __name__ == "__main__":
    n = 4

    edges = [
        [0, 1],
        [0, 2],
        [0, 3]
    ]

    labels = ['r', 'o', 't', 'e']

    s = "tr"

    sol = Solution()
    result = sol.countPrefixPaths(n, edges, labels, s)

    print("\n最终结果:", result)