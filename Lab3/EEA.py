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
    print("gcd(", a, b, ") = ", r[i - 1])
    print("Coefficient S = ", s[i - 1])
    print("Coefficient T = ", t[i - 1])
    return array


print("1) ")
eea(11069529223, 188351587)

print("2) ")
eea(435985, 288651)
