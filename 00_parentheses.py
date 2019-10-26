
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
    for c in task1:
        if c.upper() in vowels:
            task1 = task1.replace(c, "*")
    return task1
print(task2)

