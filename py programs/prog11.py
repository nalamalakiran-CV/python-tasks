"""Check if a reverse of a string is matching with the given string"""

s = input("enter the string")

def is_palindrome(s):
    i = 0 #i will be starting from the left side of the sting
    j = len(s)-1 #j will be starting from right side of the string
    while i<j:
        while not s[i].isalnum() and i<j: #condition for ignoring the special characters
            i+=1 #if any special character found it will skip that and iterate
        while not s[j].isalnum() and i<j:
            j-=1
        if s[i].lower()!=s[j].lower(): #if the starting letter and the end letter are not matching it will be terminating
            return False

        i+=1
        j-=1
    return True
print(is_palindrome(s))