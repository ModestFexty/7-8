s = input()
if 'x' not in s: 
    print('not x')
if  'w' not in s:
    print('not w')
for i in s:
    if i in 'xw':
        print(i,'встречается раньше')
        break