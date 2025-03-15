def ave(a, b):
    result = (a + b) / 2

def ave_p(a, b):
    result = (a + b) / 2
    print("p", result)

def ave_r(a, b):
    result = (a + b) / 2
    return result

def ave_pr(a, b):
    result = (a + b) / 2
    print("pr", result)
    return result

res = ave(1, 2)
res_p = ave_p(1, 2)
res_r = ave_r(1, 2)
res_pr = ave_pr(1, 2)