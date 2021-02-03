# Simple python program to count
# occurrences of pat in txt.
def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            res += 1
            j = 0
    print(res)


countFreq("bcb", "abcbcbcbcbcb")

# difference between the normal counnt and the traditional count
print("abcbcbcbcbcb".count("bcb"))
