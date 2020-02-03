import string
result = 0
print(sum([result+string.ascii_lowercase.index(e) for e in input("Enter a string: ")]))
