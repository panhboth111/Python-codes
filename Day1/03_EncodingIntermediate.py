alphabets = 'abcdefghijklmnopqrstuvxyz'
sum = 0
string = str(input())
string = string.lower()
for i in string:
    sum += alphabets.index(i)
print(sum)
