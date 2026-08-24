numbers_list = [26, 39, 51, 53, 57, 79, 85]

for number in numbers_list:
    number_factors =[]
    for i in range(2,number):
        if number % i == 0:
            number_factors.append(i)
    if len(number_factors) == 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        print("the Number factors")
        print(number_factors)



