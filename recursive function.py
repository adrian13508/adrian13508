def recursive_function(n):

    if n > 0:
        while n != 0:
            print(n)
            n -= 1
    
    else:
        while n != 2:
            print(n)
            n += 1


recursive_function(int(input()))
