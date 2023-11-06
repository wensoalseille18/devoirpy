from random import choice, randrange
import string
# str  #1

majiskil="Ayiti Se Bon Peyi"
print(majiskil+"\n")
majiskil=majiskil.lower()
print("mete en miniskil    \n :",majiskil+"\n")
# #2
chenn="je suis wenso etudiant a l'esih"
print(chenn+"\n")
lischenn=chenn.split(" ")
print("koupe chenn nan tout kote ki gen espas epi metel nan yon lis \n",lischenn)
print("\n")
# #3
print(chenn+"\n")
chenn=chenn.title()
print("premye lèt chak mo an majiskil \n ",chenn+"\n")

# #4
print(chenn+"\n")
mo=chenn[0]
for i in range(len(chenn)):
    if chenn[i]==" ":
        mo+=chenn[i+1]
print("nouvo chenn ak inisyal chak mo.\n",mo+"\n")

# #5
print(chenn+"\n")
chenn=chenn.replace('a','@')
print("Ranplase a pa @ \n",chenn+"\n")

# #6 
m2="ayiti"
print(m2+"\n")
print("enves chenn nan \n",m2[::-1].upper()+"\n")
#7  
chenn1="Ayiti kapab avanse"
print( "Afiche endeks premye karaktè  `a`  \n",chenn1+"\n",chenn1.index('a'),"\n")
#8
print(chenn1)
sindex=0
for index ,i in enumerate( chenn1):
    if i=='A' or i=='a':
        sindex+=index
print("total tout endeks karaktè  `a` yo \n",sindex,"\n")
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
print("retire espas epi kontrole \n",chenn+str(chenn.__len__()),"\n")

#list #1
listeeleman2=[]
n=input("antre yon nonb pou entèval lis la")
for i in range(int(n)+1):
    if i%2==0:
        listeeleman2.append(i)
print("lis eleman ki divizib pa 2\n"+listeeleman2,"\n")
#2
for index, i in enumerate (listeeleman2):
    listeeleman2[index]=str(i)
print("lis antye an yon lis chenn\n",listeeleman2 ,"\n")
##3
print(lischenn,"\n")
for index,i in enumerate(lischenn):
    lischenn[index]=i.upper()
print("lis la an majiskil\n",lischenn,"\n") 
# #4
lischenn22=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(lischenn22,"\n")
lischenn223=[]
for index,i in enumerate(lischenn22):
    if index % 3==0:
        lischenn223.append(lischenn22[index])
print("eleman ki nan endèks ki divizib pa 3 yo sèlman\n",lischenn223,"\n") 
# #5
print(lischenn22,"\n")
lischenn224=[]
for i in range(0, len(lischenn22), 3):
    lischenn224.append(tuple(lischenn22[i:i+3]))
print("lis ki gen chak 3 eleman yo gwoupe anndan yon tipl\n",lischenn224,"\n")
##6
lisdoublon=[1,1,2,2,3,3,4,4,5,6,6,7,7]
lissandoublon=list(set(lisdoublon))
print("lis san doublon\n",lissandoublon)
##7
lis1=[1,2,3,4,5,6,9,7,8,0]
lis2=[2,4,6,8,10]
print(lis1,lis2,"\n")
lis3=[]
for i in lis1:
    if i in lis2:
        lis3.append(i)
print("eleman komen lis yo\n",lis3,"\n")
##8
print(lis1,lis2,"\n")
lis4=[]
for i in lis1:
    if i not in lis2:
        lis4.append(i)
print("eleman distenge lis yo\n"lis4,"\n")
##9
dik={'wenso':17,'jean':23,'alseillle':22,'esih':88}
liskle=[]
lisele=[]
for key,i in dik.items():
    liskle.append(key)
    lisele.append(i)
print("lis eleman yo\n"lisele,"lis kle yo\n",liskle,"\n")
##10
li1=[1,2,3,4,5,6]
li=[2,4,6,8,10,12]
li2=[3,6,9,12]
liss=li+li1+lis2
liss=list(set(liss))
print("reyini twa lis san doublon\n",liss,"\n")

#dictionnaire #1
dik1={'wenso':17,'jean':23,'alseillle':22,'esih':88,'a':1,'b':2}
lisv=[]
for i,key in enumerate (dik1):
    lisv.append(dik1.get(key))
print(dik1,"\n","lis vale ki rekipere ak kle yo\n",lisv,"\n")
#    #2
itili=input("tape yon valè")
if itili[0]=='{' and itili[-1]=='}':
    print("wi li genyen  akolad")
else:
    if itili[0]=='{':
        print("non li gen akolad devan selman")
    elif itili[-1]=='}':
        print("non li  gen akolad deye selman")
    else:
        print("non li pa gen akolad ")
        
#   #3
print(dik1,"\n")
clef=""
for i,key in enumerate (dik1):
    clef+=key+" "
print("les clef :",clef)
#   #4
valeur=""
for i,val in dik1.items():
    valeur+=str(val)+" "
print("les valeurs :",valeur)
#   #5 
copidik1={}
for key,val in dik1.items():
    copidik1[key]=val
print("kopi diksyone\n",copidik1,"\n")

#    #6
dik1={'wenso':'wens','jean':'jacque','alseillle':22,'esih':88,'a':1,'b':'c'}
for key,val in dik1.items():
    if type(val)==str:
        val="_"+val+"_"
        dik1[key]=val
print("Ajoute yon  _underscore_  devan ak dèyè tout valè ki se chenn yo\n",dik1,"\n")
#     #7
dikkonpleks={"a": "12", "b": "abc", "c": "12r", "d":"90"}
dikdigit={}
for key,val in dikkonpleks.items():
    tes=True
    for i in val :
        if not i.isdigit():
            tes=False
    if tes:
        dikdigit[key]=val
print("",dikdigit)

#    #8
lisdik=[]
for key,val in dik1.items():
    b=(key,val)
    lisdik.append(b)
print("Pakouri yon lis tipl, pou w mete l sou fòm diksyonè",lisdik)
#    #9
diktuple={}
for i in lisdik:
    diktuple[i[0]]=i[1]
print(diktuple)
# #10
diksyone_1 = {"kle1": 5,"lis": ["wor", "!333"],"kle3": {4, 8, 16},'kle4':'b'}
diksyone_2 = {"kle1": 2,"lis": ["world", "!"],"kle3": {1, 2, 3},'kle4':'c'}
nouvo_diksyone = {}
for key,val in diksyone_1.items():
    if diksyone_2.get(key)!= None:
        if type(diksyone_1[key])==int==type(diksyone_2[key]):
            nouvo_diksyone[key]=diksyone_2[key]+diksyone_1[key]
        if type(diksyone_1[key])==(str) and type(diksyone_2[key])==(str):
            nouvo_diksyone[key]=str(diksyone_2[key]+diksyone_1[key])
print(nouvo_diksyone)   

# #1 fonksyon
mo=input("antre yon mo")
def enves(m):
    m1=m[::-1]
    return m1
print(enves(mo))
# #2
nonb=input("antre longe kod ou vle genere a")
nonb=int(nonb)
def kod(n):
    alfa=string.ascii_lowercase
    kod=""
    while n!=0:
        kod+=choice(alfa)
        n-=1
    return kod
print(kod(nonb))
# #3
nonb1=input("antre longe kod ou vle genere a")
nonb1=int(nonb1)
def kod(n):
    alfa=string.ascii_lowercase
    kod=""
    while n!=0:
        k=choice(alfa)
        while k in kod:
            k=choice(alfa)
        kod+=k
        n-=1
    return kod
print(kod(nonb1))
# #4
nonb2=input("antre longe kod ou vle genere a")
nonb2=int(nonb2)
def kod(n):
    alfa=string.ascii_lowercase+string.digits
    kod=""
    while n!=0:
        k=choice(alfa)
        while k in kod:
            k=choice(alfa)
        kod+=k
        n-=1
    return kod
print(kod(nonb2))
# #5
lischenn10=['wen-so','alseille22','@gmail','.com','gmail-com']
def slug(listee):
    alfa=string.ascii_lowercase+string.digits+"-"
    slug=""
    for i in listee:
        t=True
        for n in i:
            if not n in alfa:
                t=False
                break
        if t:
            slug+=i
    return slug
print(slug(lischenn10))      
# #6
mo3="wensoaa"
def separeLet(mo):
    m=mo+" "
    nouvo=""
    for i in m:
        if i !=" ":
            nouvo+=i+","
        if i==" ":
            nouvo+=i
    nouvo=nouvo.replace(", ","")
    return nouvo
print(separeLet(mo3))
# #7
afabe=string.ascii_lowercase
mo="wenso"
def kriptaj(mo):
    kripte=""
    for i in range(len(mo)):
        if i!=len(mo)-1:
            kripte+=str(afabe.index(mo[i].lower()))+"-"
        else:
            kripte+=str(afabe.index(mo[i]))
    return kripte
print(kriptaj(mo))
# #8
afabe=string.ascii_lowercase
krip="22-4-13-18-14"
def dekriptaj(mo):
    dekrip=""
    lis=mo.split("-")
    for i in lis:
        dekrip+=afabe[int(i)]
    return dekrip
print(dekriptaj(krip))
# #9
a=9
b=2
def pemite(a,b):
    s=a
    a=b
    b=s
    tupe=(a,b)
    return tupe
print(pemite(a,b))
# #10
non="Jean-Baptiste Jean"
def inisyal(non):
    no=non.replace("-"," ").strip()
    ini=no[0]
    for i in range(len(no)):
        if no[i]==" ":
            ini+=no[i+1]
    return ini 
print(inisyal(non)) 
