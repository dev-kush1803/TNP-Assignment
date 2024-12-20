# Comprehension

ls = {'john':24,'sam':65,'mac':22,'peter':35,'jack':20}
out1 = {'sam':65,'peter':35}
out2 = {'john':24,'mac':22,'jack':20}
o1 = {}
o2 = {}
for key,val in ls.items():
    if val < 25:
        o2[key] = val
    else:
        o1[key] = val
print(o1)
print(o2)        

o3 = {key:val for key,val in ls.items() if val < 25}
o4 = {key:val for key,val in ls.items() if val >= 25}
print(o3)
print(o4)

ls1 = [54,68,59,24,36,48,54,59,68,10,24,26,25]
res = []
for i in ls1:
    if i <25:
        res.append(i)
print(res)

res1 = [ab for ab in ls1 if ab < 25]
res2 = [ab for ab in ls1 if ab >= 25]
print(res1)
print(res2)

#WAP to remove duplicates from given list
res4 = []
for i in ls1:
    if i not in res4:
        res4.append(i)
print(res4)

print(list(set(ls1)))

se = {i for i in ls1}
print(se)
print("#" * 20)

#WAP to find 100 in given list and replace it by 200
ls2 = [10,100,23]
for i,j in enumerate(ls2):
    if j == 100:
        ls2[i] = 200
print(ls2)
for i in enumerate(ls2):
    if i[1] == 100:
        ls2[i[0]] = 200


        
