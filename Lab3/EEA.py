from random import randint
import math


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


a = eea(11069529223, 188351587)
print("1) ", a[0])

a = eea(435985, 288651)
print("2) ", a[0])


# This part does not work yet
def inverse(a, b):
    array = eea(a, b)
    # print(a)
    if array[0] == 1:
        x = 0  # This is a place holder - need to figure out what the proper use of EEA would be in this context
    else:
        print("a is not invertible")
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


print("3) ", inverse(300, 104759))

print("4) ", inverse(300, 104003))


# This part does not work yet
def fermat(n, k):
    i = 0
    found = False
    j = 0

    while i < k:
        count = randint(0, i) + 2
        if count ^ (n - 1) != 1 % n:
            print("composite")
            found = True
            j += 1
            break
        i += 1

    if not found:
        print("Probably prime")
        print("Count: ", j)


# This part does not work yet
def miller(n, k):
    i = 0
    j = 1
    found = False

    while i < k:
        count = randint(0, i) + 2

        print(count)
        # unsure how to get this info in correct order
        r = (n - 1)/(2 ^ u)
        u = math.log2((n-1)/r)
        z = count ^ r % n

        if z != 1 & z != n-1:
            while j < u - 1:
                z = z ^ 2 % n
                if z == 1:
                    print(n, "is composite")
                    found = True
            if z != n-1:
                print(n, "is composite")
                found = True

        i += 1
    if not found:
        print(n, "is likely prime")


# Causes memory error
fermat(9746347772161, 1)

# Causes memory error
miller(9746347772161, 1)

