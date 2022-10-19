l = []
maximums = []
res = []
for item in operations:
    lst = item.split(' ')  # ['1', '97']
    operation_type = int(lst[0])
    if operation_type == 1:
        num = int(lst[1])
        l.append(num)
        if not maximums or num >= maximums[-1]:
            maximums.append(num)
    elif operation_type == 2:
        popped = l.pop()
        if maximums[-1] == popped:
            maximums.pop()
    elif operation_type == 3:
        res.append(maximums[-1])
return res

