# str  #1
majiskil="Ayiti Se Bon Peyi"
print(majiskil+"\n")
majiskil=majiskil.lower()
print(majiskil+"\n")
# #2
chenn="je suis wenso etudiant a l'esih"
print(chenn+"\n")
lischenn=chenn.split(" ")
print(lischenn)
print("\n")
# #3
print(chenn+"\n")
chenn=chenn.title()
print(chenn+"\n")

# #4
print(chenn+"\n")
mo=chenn[0]
for i in range(len(chenn)):
    if chenn[i]==" ":
        mo+=chenn[i+1]
print(mo+"\n")

# #5
print(chenn+"\n")
chenn=chenn.replace('a','@')
print(chenn+"\n")

# #6 
m2="ayiti"
print(m2+"\n")
print(m2[::-1].upper()+"\n")
#7  
chenn1="Ayiti kapab avanse"
print( chenn1+"\n",chenn1.index('a'),"\n")
#8
print(chenn1)
sindex=0
for index ,i in enumerate( chenn1):
    if i=='A' or i=='a':
        sindex+=index
print(sindex,"\n")
#9
print(chenn1)
liste=[]
for index ,i in enumerate( chenn1):
    if   i=='a':
        liste.append(index)
print(liste,"\n")
#10
chenn="je suis wenso etudiant a l'esih"
print(chenn+"\n")
chenn=chenn.replace(" ","")
b=0
for i in chenn:
    b+=1
chenn+=str(b)
print(chenn+"\n")

#list #1
listeeleman2=[]
n=input("antre yon nonb pou entèval lis la")
for i in range(int(n)+1):
    if i%2==0:
        listeeleman2.append(i)
print(listeeleman2,"\n")
#2
for index, i in enumerate (listeeleman2):
    listeeleman2[index]=str(i)
print(listeeleman2 ,"\n")
##3
print(lischenn,"\n")
for index,i in enumerate(lischenn):
    lischenn[index]=i.upper()
print(lischenn,"\n") 
# #4
lischenn22=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(lischenn22,"\n")
lischenn223=[]
for index,i in enumerate(lischenn22):
    if index % 3==0:
        lischenn223.append(lischenn22[index])
print(lischenn223,"\n") 
# #5
print(lischenn22,"\n")
lischenn224=[]
for i in range(0, len(lischenn22), 3):
    lischenn224.append(tuple(lischenn22[i:i+3]))
print(lischenn224,"\n")
##6
lisdoublon=[1,1,2,2,3,3,4,4,5,6,6,7,7]
lissandoublon=set(lisdoublon)
print(lissandoublon)
##7
