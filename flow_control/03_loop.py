
# for ... in:
# for element in iterable
#       dothings

# range() has 3 paras: start, stop, steps
for i in range(10):
    print(i)
print('----------')


for i in range(1,5):
    print(i)
print('----------')


for i in range(10,2,-2):
    print(i)
print('----------')

# using for loop to iterate
l = [4,5,9,123,421,945]
for n in l:
    print(n)
print('----------')

# enumerate(iterable, start=0)
# return a tuple containing a count and the values
l = [4,5,9,123,421,945]
for i, n in enumerate(l):
    print(f'Index:{i}, Number:{n}')