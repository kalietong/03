
ex = (input("type something "))

def task1(s):
    ret = ""
    i = True
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char !=' ':
            i = not i
    return ret
print(task1(ex))

def task2(task1):
    vowels = ('A','E', 'I', 'O', 'U')
    for c in task1(ex):
        if c in vowels:
            res = taskl(ex).replace(c, "*")
    return res
print(task2(task1))

