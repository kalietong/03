
ex = input("type something ")

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

def task2(s):
    word = task1(ex)
    vowels = ('A','E', 'I', 'O', 'U')
    for vowels in vowels:
            word = word.replace(vowels, "*")
    return word
print(task2(ex))

def check_parentheses(ex):
    word = task1(ex)
    if word.count("(") == word.count(")"):
        print("balanced? True")
    else:
        print("balanced? False")
    return ""

print(check_parentheses(ex))
