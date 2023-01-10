class Solution(object):
    def isIsomorphic(self, s, t):
        # one-way mapping with s as key
        map = {}
        for i in range(len(s)):
            if s[i] not in map.keys():
                map[s[i]] = t[i]
            else:
                if map[s[i]] != t[i]:
                    return False
        # handle mapping with t as key
        return len(set(list(s))) == len(set(list(t)))


def main():
    solution = Solution()
    s = "badc"
    t = "baba"
    print(solution.isIsomorphic(s, t))


if __name__ == "__main__":
    main()