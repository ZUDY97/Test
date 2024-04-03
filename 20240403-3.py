def plus(v1, v2, v3):
    result = v1 + v2 + v3
    return result

hap = plus(100, 200, 300)
print(hap)


def f1():
    print(var)

def f2():
    var = 10
    print (var)

var = 100
f1()
f2()


def myFunc(P1=0, P2=0, P3=0):
    ret = P1 + P2 + P3
    return ret

print("매개변수 없이 호출==>", myFunc())
print("매개변수가 1개로 호출==>", myFunc(1))
print("매개변수가 2개로 호출==>", myFunc(1, 2))
print("매개변수가 3개로 호출==>", myFunc(1, 2, 3))
