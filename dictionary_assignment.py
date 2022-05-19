Dic = {}

while True : 
    key = int(input("key: "))
    value = str(input("value: "))
    Dic[key] = value
       
    if ( (key == 0)):
        print("그만")
        print(Dic)
        break
    elif ( ( value == '문자열 종료')):
        print("그만")
        print(Dic)
        break

print("dict_keys 객체 리스트 변환 출력: ", list(Dic.keys()))
print("dict_values 객체 리스트 변환 출력: ", list(Dic.values()))
print("dict_items 객체 리스트 변환 출력: ", list(Dic.items()))