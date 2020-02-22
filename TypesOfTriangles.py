run = True
print("Identifying Types of Triangle.")
while run:
    sideA = float(input("Enter measurement for Side A (cm): "))
    sideB = float(input("Enter measurement for Side B (cm): "))
    sideC = float(input("Enter measurement for Side B (cm): "))

    if sideA == sideB and sideB == sideC:
        print("The Triangle is an Equilateral Triangle.")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print("The Triangle is an Isosceles Triangle.")
    else:
        print("The Triangle is a Scalene Triangle.")

    runAgain = int(input("Run the program again? [1] Yes [2] No: "))
    if runAgain == 1:
        run = True
    else:
        run = False
print("Thank you for running the program")
