first=0
second=1
print(first)
print(second)
for a in range(1,19):
    third=first+second
    print(third)
    first,second=second,third
