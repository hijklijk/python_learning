# function: sorted()
# method: sort(), reverse()

dest = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hangzhou']
print(dest)

print('\n--sorted--')
print(sorted(dest))
print(dest)

print('\n--sorted(reversed)--')
print(sorted(dest,reverse=True))
print(dest)

print('\n--reverse--')
dest.reverse()
print(dest)

print('\n--reverse(back)--')
dest.reverse()
print(dest)

print('\n--sort--')
dest.sort()
print(dest)

print('\n--sort(reversed)--')
dest.sort(reverse=True)
print(dest)

