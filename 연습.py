num1, num2, num3 = map(int, input().split())
list1 = []
list1.append(num1)
list1.append(num2)
list1.append(num3)


if num1 ==num2 and num1 ==num3:
    print(10000+num1*1000)

elif num1 ==num2:
    print(1000+num1*100)

elif num1==num3:
    print(1000+num1*100)

elif num2 ==num3:
    print(1000+num2*100)

else:
    print(max(list1)*100)
