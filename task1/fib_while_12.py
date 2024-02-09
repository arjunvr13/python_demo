limit = 10
first = 0
second = 1
print(first, end=",")
print(second, end=",")
i = 0
while i< limit-2:
    third = first + second
    print(third, end=",")
    first = second
    second = third
    i += 1