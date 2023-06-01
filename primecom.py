def primenum(number):
    c = 0
    for num in range(1, number+1):
        if number % num == 0:
            c += 1
    if c == 2:
        print(f"{number} is prime")
    else:
        print(f"{number} is composite")

primenum(number=int(input("Enter the number of your choice")))