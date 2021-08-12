def has_odd(integers):
    tokens = []
    split_integers = integers.split()
    tokens = [int(i) for i in split_integers]
    for i in tokens:
        if (i % 2 != 0) and (len(tokens) >=1):
            print('True')
            return True
        else:
            print('False')
            return False


has_odd(input('Enter integers:'))