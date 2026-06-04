def build_next(s):
    n = len(s)
    nxt = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = nxt[j - 1]

        if s[i] == s[j]:
            j += 1

        nxt[i] = j

    return nxt

print(build_next("abaabcabaabcabcab"))