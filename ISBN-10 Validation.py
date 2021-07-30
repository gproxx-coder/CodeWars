
# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python

def valid_ISBN10(isbn):
    total = 0
    if len(isbn) == 10:
        for idx in range(1, len(isbn)):
            if 48 <= ord(isbn[idx-1]) <= 57:
                total += int(isbn[idx-1]) * idx
            else:
                return False
        if isbn[-1] == 'X':
            total += 10 * 10
        else:
            total += int(isbn[-1]) * 10
        return True if total % 11 == 0 else False
    return False




print(valid_ISBN10('1112223339')) #, True)
print(valid_ISBN10('048665088X')) #, True)
print(valid_ISBN10('1293000000')) #, True)
print(valid_ISBN10('1234554321')) #, True)
print(valid_ISBN10('1234512345')) #, False)
print(valid_ISBN10('1293')) #, False)
print(valid_ISBN10('X123456788')) #, False)
print(valid_ISBN10('ABCDEFGHIJ')) #, False)
print(valid_ISBN10('XXXXXXXXXX')) #, False)
