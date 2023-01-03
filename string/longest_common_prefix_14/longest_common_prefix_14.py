def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    num_strs = len(strs)
    result = ""
    i = 0
    common = True

    while common:
        for j in range(num_strs - 1):
            if strs[j] == "":
                return ""

            try:
                if strs[j][i] != strs[j + 1][i]:
                    print(strs[j])
                    common = False
                    break
            except IndexError:
                common = False
                break
        if common:
            result += strs[0][i]
        i += 1
    return result

strs = ["ab", "a"]
print(longestCommonPrefix(strs))