a=int(input('Введите меньшее число '))
b=int(input('Введите большее число '))
for i in range (a,b+1):
    if i%2==0:
        print(i,end=' ')
