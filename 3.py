s1='g.txt'
s2='r.txt'
#s1=input()
#s2=input()
f1=open(s1)
name=[]#id, nazv, company
m1=f1.readline()
while True:
    m1=f1.readline().split(';')
    if m1==['']:
        break
    m1[0]=int(m1[0])
    m1[2]=m1[2][:-1]##################
    name.append(m1)
f1.close()
res=[]#id, kol-vo mark, summa mark, sr, nazv, comp
for i in range(len(name)):
    res.append([name[i][0],0,0,0,name[i][1],name[i][2]])
f2=open(s2)
m1=f2.readline()
while True:
    m1=f2.readline().split(';')
    if m1==['']:
        break
    m1[0]=int(m1[0])
    m1[1]=int(m1[1])
    for x in res:
        if x[0]==m1[0]:
            x[1]+=1
            x[2]+=m1[1]
            break
f2.close()
for x in res:
    x[3]=x[2]/x[1]
res.sort(key=lambda x: x[3])
res=res[::-1]
for i in range(3):
    t=res[i]
    print(t[4],round(t[3],3))#############
comp=[]
k8=[]
for i in range(len(name)):
    c=name[i]
    if c[2] not in comp:
        comp.append(c[2])
for i in range(len(comp)):
    k8.append(0)
for i in range(len(res)):
    if res[i][3] > 8:
        k8[comp.index(res[i][5])]+=1
    else:
        break
ma=max(k8)
ima=k8.index(ma)
print(comp[ima],ma)
