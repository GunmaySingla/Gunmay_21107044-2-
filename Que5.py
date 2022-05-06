sideA = float(input('Enter length A-\n'))
sideB = float(input('Enter length B-\n'))
sideC = float(input('Enter length C-\n'))

side_A = int(round(sideA))
side_B = int(round(sideB))
side_C = int(round(sideC))

a = side_A + side_B
b = side_B + side_C
c = side_C + side_A

condition_1 = a > side_C
condition_2 = b > side_A
condition_3 = c > side_B

ans = str(condition_1 & condition_2 & condition_3)

ans = ans.replace('True','Yes')
ans = ans.replace('False','No')

print ('Do the values input by the user form a triangle-:')
print (ans)