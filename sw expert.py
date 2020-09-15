T = int(input())
count = 1
for i in range(T):
    case = int(input())
    name_list = []
    for j in range(case):
        name = str(input())
        name_list.append((name, len(name)))
print(name_list)