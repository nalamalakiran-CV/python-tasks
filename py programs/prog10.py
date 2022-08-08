"""There are two lists one is having multiple words and another is having
    keywords now we have to check which keyword is present in first list"""


l1=['hello', 'world', 'welcome', 'python', 'list']
l2=['ll', 'rl', 'lc', 'py', 'is']
s1=" ".join(l1)
print(s1)
l3 =[]
for i in l2:
    if i in s1:
        l3.append(i)

print("key words in l are", l3)