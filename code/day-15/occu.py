def count(s, c) :

    # Count variable
    res = 0

    for i in range(len(s)) :

        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res


# Driver code
str= "abbseeeeeaccc"
c = 'c'

print(count(str, c))
