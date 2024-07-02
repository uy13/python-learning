for number in range(1, 101):
    three = (number % 3 == 0) * 'Fizz'
    five = (number % 5 == 0) * 'Buzz'
    print((three + five) or number)
