# if, elif, else
# please add : at the end of a line using this command
a = 4
b = 3

# only if
if a:
    print('condition is true, a =',a)

# if and else
if a<2:
    print('condition is true')
else:
    print('condition is not true')

# if, else, elif
if a < b:
    print(f'Number A {a} is smaller than number B {b}')
elif a == b:
    print(f'Number A {a} is equal to number B {b}')
else:
    print(f'Number A {a} is bigger than number B {b}')

# conditional expressions
# and, or
c = 0
d = 5
if c > 0 or d > 0:
    print('include at least one positive number');
else:
    print('both are not positive numbers')

