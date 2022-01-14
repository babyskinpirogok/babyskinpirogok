import random
a = str(chr(random.randint(65, 72))) + str(random.randint(1, 8)) + \
    "-" + str(chr(random.randint(65, 72))) + str(random.randint(1, 8))
a = list(a)
print(a)
a = ["A", "1", "-", "A", "1"]
c = 0


def con(a):
    if ord(a[0]) + int(a[1]) - ord(a[3]) - int(a[4]) == 3:
        if ord(a[0]) - ord(a[3]) == 2 and int(a[1]) - int(a[4]) == 1:
            return True
        elif ord(a[0]) - ord(a[3]) == 1 and int(a[1]) - int(a[4]) == 2:
            return True
        else:
            return False
    elif ord(a[0]) + int(a[1]) - ord(a[3]) - int(a[4]) == 1:
        if ord(a[0]) - ord(a[3]) == -1 and int(a[1]) - int(a[4]) == 2:
            return True
        elif ord(a[0]) - ord(a[3]) == 2 and int(a[1]) - int(a[4]) == -1:
            return True
        else:
            return False
    elif ord(a[0]) + int(a[1]) - ord(a[3]) - int(a[4]) == -1:
        if ord(a[0]) - ord(a[3]) == -2 and int(a[1]) - int(a[4]) == 1:
            return True
        elif ord(a[0]) - ord(a[3]) == 1 and int(a[1]) - int(a[4]) == -2:
            return True
        else:
            return False
    elif ord(a[0]) + int(a[1]) - ord(a[3]) - int(a[4]) == -3:
        if ord(a[0]) - ord(a[3]) == -2 and int(a[1]) - int(a[4]) == -1:
            return True
        elif ord(a[0]) - ord(a[3]) == -1 and int(a[1]) - int(a[4]) == -2:
            return True
        else:
            return False
    else:
        return False


def ladia(a):
    if a[0] == a[3] or a[1] == a[4]:
        return True
    else:
        return False


def slon(a):
    if abs(ord(a[0]) - ord(a[3])) == abs(int(a[1]) - int(a[4])):
        return True
    else:
        return False


def ferse(a):
    if ladia(a) or slon(a):
        return True
    else:
        return False


def corol(a):
    if abs(ord(a[0]) - ord(a[3])) == 1 and abs(int(a[1]) - int(a[4])) == 1:
        return True
    elif abs(ord(a[0]) - ord(a[3])) == 1 and abs(int(a[1]) - int(a[4])) == 0:
        return True
    elif abs(ord(a[0]) - ord(a[3])) == 0 and abs(int(a[1]) - int(a[4])) == 1:
        return True
    else:
        return False


def peshka(a):
    if a[0] == a[3]:
        if int(a[1]) == 1:
            return False
        elif int(a[1]) == 2:
            if int(a[1]) - int(a[4]) == -2:
                return True
            elif int(a[1]) - int(a[4]) == -1:
                return True
    else:
        return False

if a[0] == a[3] and a[1] == a[4]:
    print("Nobody")
else:
    if peshka(a):
        print("Pawn")
        c += 1
    if corol(a):
        print("King")
        c += 1
    if slon(a):
        print("Bishop")
        c += 1
    if ferse(a):
        print("Queen")
        c += 1
    if ladia(a):
        print("Rook")
        c += 1
    if con(a):
        print("Knight")
        c += 1
    if c == 0:
        print("Nobody")
