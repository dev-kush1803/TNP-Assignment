def even():
    ev = []
    for i in range(1,120):
        if i % 2 == 0:
            ev.append(i)
    yield ev

res = even()

#for i in res:
#    print(i)
print(next(res))

ls = [x for x in range(1,11)]
print(ls)

tu = (x for x in range(1,11))
print(tu)
print(next(tu))
print(next(tu))

def show():
    a = "Hello"
    yield a

    b = "BYE"
    yield b

    c = "HI"
    yield c
    return a,b,c

x = show()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

