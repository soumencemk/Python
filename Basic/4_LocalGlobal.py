f = 101  # GLOBAL


def someFunc():
    global a
    a = 300
    f = 100  # LOCAL
    print(f)


def someOtherFunc():
    f = "SOUMEN KARMAKAR"
    print(f)


someFunc()
someOtherFunc()
print(f)
print(a)
del a
# print(a) -- Error