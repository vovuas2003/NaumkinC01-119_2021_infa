s1='g.txt'
s2='r.txt'
#s1=input()
#s2=input()
f1=open(s1)
name=[]
m1=f1.readline()
while True:
    m1=f1.readline().split(';')
    if m1==['']:
        break
    m1[0]=int(m1[0])
    m1[2]=m1[2][:-1]
    name.append(m1)
f1.close()
res=[]#id, kol-vo mark, summa mark, sr
for i in range(len(name)):
    res.append([name[i][0],0,0,0])
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
print(res)
