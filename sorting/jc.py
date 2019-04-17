def jc(n):
    res = 1
    if n > 1:
        res = n * jc(n-1)
    return res


print(jc(5))
