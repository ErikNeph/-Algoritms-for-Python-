def fact(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return x * fact(x-1)


print(fact(5)) # 5! = 5 * 4 * 3 * 2 * 1
