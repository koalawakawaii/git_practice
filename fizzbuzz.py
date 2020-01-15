def fizzbuzz_conbert(number):
    if number % 15 == 0:
        return "fizzbuzz"

    if number % 3 == 0:
        return "fizz"

    if number % 5 == 0:
        return "buzz"

    return str(number)


for number in range(1, 101):
    print(fizzbuzz_conbert(number))

assert fizzbuzz_conbert(3) == "fizz"
