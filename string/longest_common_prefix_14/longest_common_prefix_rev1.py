def longestCommonPrefix(strs):
    # Find the smallest length of string
    if len(strs) == 0:
        return ""

    min_length_str = min(strs, key=len)
    i = 0
    common = True
    result = ""

    while i < len(min_length_str):
        for j in range(len(strs) - 1):
            if strs[j] == "":
                return result

            if strs[j][i] != strs[j + 1][i]:
                common = False
                break
        if common:
            result += strs[0][i]
        i += 1
    return result

strs = ["flower","flow","flight"]
strs2 = ["ab","a"]
strs3 = ["",""]

print(longestCommonPrefix(strs))
print(longestCommonPrefix(strs2))
print(longestCommonPrefix(strs3))