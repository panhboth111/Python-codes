#ord(): built-in function to convert characte to ascii value 
#chr(): built-in functions to convert ascii value to Character.
sum =0
i =0
Input = str(input())
for i in Input:
    sum += ord(i)
print(sum)
