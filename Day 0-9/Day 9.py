def factorial(num):
    q = 1 
    for i in range(1,num+1):
        q = i * q 
    print(q)
factorial(int(input()))
