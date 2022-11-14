s1 = input()
s2 = input()
a = abs(len(s1)-len(s2))
if len(s1) > len(s2):
    print('первая больше')
else:
    print('вторая больше')
print('на',a,'символов')    