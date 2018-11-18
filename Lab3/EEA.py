def eea(a, b):
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    q = [0]
    i = 1

    while r[i] != 0:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(0)
        q[i - 1] = (r[i-2] - r[i]) / r[i - 1]
        s.append(s[i - 2] - q[i - 1] * s[i - 1])
        t.append(t[i - 2] - q[i - 1] * t[i - 1])

    array = [r[i - 1], s[i - 1], t[i - 1]]
    # print("gcd(", a, b, ") = ", r[i - 1])
    # print("Coefficient S = ", s[i - 1])
    # print("Coefficient T = ", t[i - 1])
    return array


print("1) ")
a = eea(11069529223, 188351587)
print(a[0])

print("2) ")
a = eea(435985, 288651)
print(a[0])


# This part does not work yet
def inverse(a, b):
    array = eea(a, b)
    # print(a)
    if array[0] == 1:
        x = 0  # This is a place holder - need to figure out what the proper use of EEA would be in this context
    else:
        print("a is not invertible")
    print(x)
    '''
    t = 0
    r = b
    newt = 1
    newr = a

    while newr != 0:
        quotient = r % newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    print(r)

    if r > 1:
        print("A is not invertible")

    if r < 0:
        t += b
        print(t)
    '''


print("3) ")
inverse(300, 104759)
print("4) ")
inverse(300, 104003)
