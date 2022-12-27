def solution(n,a,b):
    if a > b:
        a, b = b, a

    count = 1 
    while True:
        if b % 2 == 0 and a + 1 == b:
            break    
        a = a//2 + a%2
        b = b//2 + b%2
        count += 1
    return count