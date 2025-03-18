def reorganiser_chaine(s):
    s_pas_changer = s
    s = sorted(s)
    res = ""
    for i in range(0, len(s), 2):
        res += s[i]
    for i in range(1, len(s), 2):
        res += s[i]
   
    if res == s_pas_changer:
        return ""
    else:
        return res

print(reorganiser_chaine("aabb"))
