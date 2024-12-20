#WAP to reverse a string
inp1 = "hello"
out1 = "olleh"
res = ''
for i in inp1: # e
    res = i + res # olleh

print(res)

#WAP to check given string is palindrom or not
if inp1 == res:
    print("Given string is palindrom")
else:
    print("Given string is not palindrom")


#WAP to count vowels and consonant in given string
st = "Hello I Am leaning Python in punjab"
x = 0
y = 0
for i in st.lower():
    if i.isalpha():
        if i in 'aeiou':
            x += 1
        else:
            y += 1

#WAP to remove adjacent duplicate from given string
# inp = "aaababcca", output = "ababa"
'''
input = "aaababcca"

output = ""
i = 0
while i < len(input)-1 :
    if input[i] == input[i+1] :
        i += 1
    else:
        output += input[i]
    i+=1
output += input[len(input)-1] 
print(output)
'''
'''
def removeAdjacent(s):
    lst=list(s)
    lst2=[]
    for i in range(len(lst)-2):
        if lst[i]==lst[i+1]:
            lst2.append(i)
    for j in lst2:
        lst.pop(j)
    s=str(lst)
if __name__=="__main__":
    s="aaabbabcca"
    removeAdjacent(s)
    print(s)
'''

ls = ['a','b','c']
s = ''
for i in ls:
    s += i
lst = ['25','02','2001']
st = '/'.join(ls)




