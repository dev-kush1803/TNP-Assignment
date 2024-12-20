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


