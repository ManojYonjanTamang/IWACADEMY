d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_status(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
key_status(5)
key_status(10)
