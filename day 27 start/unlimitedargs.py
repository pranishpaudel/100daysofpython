add = 0

def adi(*insa):
    global add
    for addd in insa:
        add += addd

adi(5, 6, 2, 5, 5, 5)
print(add)  # Output will be 28
