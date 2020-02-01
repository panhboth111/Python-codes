vowels = ['a','e','i','o','u']
s = "".join(list(map(lambda x: x.upper() if(x in vowels) else x.lower(),list(input().replace(" ","").lower()))))
print(s)

