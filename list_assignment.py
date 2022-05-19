List = []

for x in range(0, 15):
    num = int(input())
    List.append(num)
    if ( num == 15 ):
        print(List)

for x in List:
    if ( x % 2 == 0 ):
        List.remove(x)

print(List)

for x in List:
    if ( x % 3 == 0 ):
        List.remove(x)

print(List)

print(List.pop(0))
List.insert(0, 2)
List.insert(1, 3)
print(List)