# user input, user should enter numbers
numbers = input("Enter some numbers separated by spaces: ")

# program splits the input into separate values
numbers = numbers.split()

prime_numbers = []
composite_numbers = []
neither_numbers = []

# check values
for number in numbers:

    try:
        number = int(number)

        # 0, 1 and negative numbers are neither
        if number < 2:
            neither_numbers.append(number)

        else:
            is_prime = True

            # check to see if the number can be divided by another number
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            # add the number to the right list
            if is_prime:
                prime_numbers.append(number)
            else:
                composite_numbers.append(number)

    except ValueError:
        # add non integers to this list
        neither_numbers.append(number)

# list the results
print("Prime numbers:", prime_numbers)
print("Composite numbers:", composite_numbers)

print("Neither:", neither_numbers)
