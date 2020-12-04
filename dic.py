# dic
dic = {
    'kimi':'pm',
    'sunny':'pc',
    'lichan':'engg',
    'tianyang':'pm',
    'conor':'engg'
}

not_pm = ['pc','engg']
for name, job in dic.items():
    print(f'{name}\'s job is {job}')
    if job not in not_pm:
        print('--it is pm job!')
else:
    print('all done')

for name,job in sorted(dic.items()):
    print(name,job)
print(dic)