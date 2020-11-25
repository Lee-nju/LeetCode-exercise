def func(code):
    if not code or len(code) == 1:
        return 1

    if int(code[0]) != 0 and eval(code[:2]) <= 25:
        return func(code[1:]) + func(code[2:])
    else:
        return func(code[1:])


s = input()
code = ''
for ch in s:
    code = code + str(ord(ch) - 65)

res = func(code) - 1
print(res)
