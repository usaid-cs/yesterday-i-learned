def twoStrings(s1, s2):
    # Write your code here
    chars1 = set(list(s1))
    chars2 = set(list(s2))
    if chars1 & chars2:
        return "YES"
    return "NO"
