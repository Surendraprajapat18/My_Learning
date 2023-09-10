def fun(a, b, *args):
    sm = 1
    for i in args:
        sm *= i
    return sm

z = fun(1,2,3,4,5)
print(z)