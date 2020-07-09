def is_leap(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        return True
    return False


year = int(input())
print(is_leap(year))
