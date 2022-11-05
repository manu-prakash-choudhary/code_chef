import sys
def point_finder(low, high, prev):
    if low < high - 1:
        mid = (low + high) // 2
        print("? {} {}".format(mid, 0))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            return point_finder(mid, high, inp)
        else:
            return point_finder(low, mid, inp)
    elif prev == "NO":
        return high, prev
    return low, prev

def base_finder(low, high, prev):
    if low < high - 1:
        mid = (high + low) // 2
        print("? {} {}".format(mid, sq_len))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            return base_finder(mid, high, inp)
        else:
            return base_finder(low, mid, inp)
    elif prev == "NO":
        return high, prev
    return low, prev

def height_finder(low, high, prev):
    if low < high - 1:
        mid = (low + high) // 2
        print("? 0 {}".format(mid))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            return height_finder(mid, high, inp)
        else:
            return height_finder(low, mid, inp)
    elif prev == "NO":
        return high, prev
    return low, prev

def main(len, temp):
    if temp == "YES":
        print("? {} {}".format(len + 1, len + 1))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            len += 1
    else:
        len -= 1
    return len
def main1(len, temp):
    if temp == "YES":
        print("? {} {}".format(len + 1, sq_len))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            len += 1
    else:
        len -= 1
    return len
def main2(len, temp):
    if temp == "YES":
        print("? 0 {}".format(len + 1))
        sys.stdout.flush()
        inp = input()
        if inp == "YES":
            len += 1
    else:
        len -= 1
    return len
sq_len, temp = point_finder(0, 1000, "YES")
sq_len = main(sq_len, temp)

sq_len *= 2
base_len, temp = base_finder((sq_len // 2), 1000, "YES")
base_len = main1(base_len, temp)

height_triangle, temp = height_finder(sq_len, 1000, "YES")
height_triangle = main2(height_triangle, temp)
height_triangle -= sq_len

area = (base_len * height_triangle) + sq_len**2
print("! {}".format(area))
# This is a new line that ends the file.
