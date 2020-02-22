print("Identifying Types of Triangle.")
sideA = float(input("Enter measurement for Side A (cm): "))
sideB = float(input("Enter measurement for Side B (cm): "))
sideC = float(input("Enter measurement for Side B (cm): "))

if sideA == sideB and sideB == sideC:
    print("The Triangle is an Equilateral Triangle.")
elif sideA == sideB or sideB == sideC or sideA == sideC:
    print("The Triangle is an Isosceles Triangle.")
else:
    print("The Triangle is a Scalene Triangle.")