
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    print("Sum of odds between 1 and 20 using 'for' loop = " + str(odd_sum))

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    print("Sum of evens between 1 and 20 using 'while' loop = " +  str(even_sum))

def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion
    if num <= 0:
        print("Sum of odds between 1 and 20 using recursion = " +  str(odd_sum))
    else:
        odd_sum = num + odd_sum
        loop1Rec(num - 2, odd_sum)


def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if num <= 0:
        print("Sum of evens between 1 and 20 using recursion = " +  str(even_sum))
    else:
        even_sum = num + even_sum
        loop1Rec(num - 2, even_sum)

loop1()
loop1Rec(19,0)
loop2()
loop2Rec(18,0)
