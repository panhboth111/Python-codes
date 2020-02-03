inp= (input("Enter Your String: ")).lower()
vowels = ['a','e','i','o','u']
string = ""
for i in inp:

    if i in vowels:
        string = string + i.upper()
    else:
        string = string + i.lower()
print(string)