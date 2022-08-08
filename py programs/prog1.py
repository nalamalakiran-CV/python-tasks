"""Given variable x = 'aaabbadcaa'
write code to get the result like- a3b2a1d1c1a2"""

s = 'aaabbadcaa'
ch = s[0]
result = ""
count = 0
s = s + " "
for x in s:
    if x == ch:
        count +=1
    else:
        result = result + str(ch)+str(count)
        ch = x
        count = 1
print(result)