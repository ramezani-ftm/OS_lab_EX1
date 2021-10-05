print('Enter the sides of the triangle:  (non-zero number)')
a = float(input())
b = float(input())
c = float(input())

if a+b<c or b+c<a or a+c<b:
        print('These 3 numbers are not acceptable.')
else:
        print('With these numbers you can make a triangle :)')