for r in range(2,21):
    for c in range(1,11):
        m=r*c
        if m<21:
            print('  ',m,'  ',end='  ')
        else:
            print(m,end='  ')
    print()
