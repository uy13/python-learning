for a in range(1, 101):
    for b in range(2, a):
        if a % b == 0:
            print(f"{a} is not prime")
            break
    else:
        print(f"{a} is prime")
