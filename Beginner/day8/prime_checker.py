def prime_checker(number):
    count = 0
    primeArr = []

    while ((len(primeArr) < 1) and (count < number)):
        for n in range(2, number):
            count += 1
            if (number % n == 0):
                primeArr.append(n)

    if (len(primeArr) > 0):
        print(f"{number} is not prime. It is divisible by {primeArr[0]}.")
    else:
        print(f"{number} is prime.")


n = int(input("Check this number: "))
prime_checker(number=n)
