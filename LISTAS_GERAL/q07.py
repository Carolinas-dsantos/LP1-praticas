a=[1,2,3,5,8,9]
def f(l):
    b = ""
    for x in a:
        b += str(x)
    return int(b)

print(f(a))