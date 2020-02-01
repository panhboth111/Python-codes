import string
alphs = string.ascii_lowercase
values = {alphs[i]:i for i in range(len(alphs))}
res = sum([values[i] for i in list(input().lower())])
print(res)