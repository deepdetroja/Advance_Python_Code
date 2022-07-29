while(True):
    print('you can exit from "q" butten.')
    a = input("enter a number :")
    if a == 'q':
        break
    try:
        a=int(a)
        if a>6:
            print('your enter a number gerter than 6')
    except Exception as a:
        print(a)
print('thanks for playing game ')
