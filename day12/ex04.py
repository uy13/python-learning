def palindrome(a):
    a = a.strip().lower()
    x = a[::-1]
    if list(x) == list(a):
        print("True")
    else:
        print("False")


palindrome("hannah")
