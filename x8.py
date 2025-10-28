def swap_first_two_digits(N):
    d =1 
    t = N
    while t>10:
        t=t // 10
        d=d * 10

    e = N // d

    a = N // d
    b = (N // (d//10))% 10

    r = N % (d//10)

    new =b * d + a * (d//10) + r

    return new
