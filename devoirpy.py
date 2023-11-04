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
