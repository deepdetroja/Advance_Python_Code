from pickle import TRUE


def greater(num):
    if num>5:
        return True
    else:
        return False
l = [1,23,3,4,5,66]
print(list(filter(greater,l)))