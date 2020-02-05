while True:
    factors = 0

    num = int(input("Enter number here: "))
    for i in range(num + 1):
        if (num % (i+1)) == 0:
            factors += 1
    if factors > 2:
        print("The number is a composite number. It has ",factors, "factors.")
    else:
        print("The number is a prime number.")
