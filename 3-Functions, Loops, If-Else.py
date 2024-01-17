#Functions

print("test")

# ?print

print("arguman1","arguman2",sep=" xxx ", end="!",flush=True)


# =============================================================================
# sep, end, flush falan bunlara kursta hoca argüman diyor ama chatgpt parametre dedi
# bence arguman olan benim arguman 1 arguman 2 dediğim kısım
# CTRL 4 çoklu yorum satırı, CTRL 1 tekli yorum satırı
# =============================================================================

3**4  #3ün 4.kuvvetini al demek

x=3
y=7

def power(x,y=1):
    return x**y

# fonskiyon return ifadesini görünce o satırda durur.
# =============================================================================
# func içindeki x ve y local, üstte belirtilen x ve y ise globaldir, ilişkileri yoktur
# python bi değeri önce localde ağar, eğer bulamazsa globalden arar  
# =============================================================================

power(5)
power(3,5)
# str(deger) degeri stringe çevirir

power(y=2,x=5)**2


value = 50000
value == 4

print("Lutfen gelirinizi giriniz")
# gelir = int(input("Gelirinizi girin"))
gelir = 100

if gelir<value:
    print("\nincome has not exceeded")
elif gelir==value:
    print("\nincome equals value")
else:
    print("\nincome exceeded")
    
    
ogrenci = ["ali","veli","ışık"]


for i in ogrenci:
    print(i)
    
    
maaslar = [14,18,20,47,79,34,48,90]

asgari_alti=0
iki_asgari_alti=0
uc_asgari_alti=0
uc_asgari_ustu=0

for i in maaslar:
    
    if (i/17)<1:
        asgari_alti+=1
    elif i/17<2:
        iki_asgari_alti+=1
    elif i/17<3:
        uc_asgari_alti+=1
    else:
        uc_asgari_ustu+=1
        
print(asgari_alti, iki_asgari_alti, uc_asgari_alti, uc_asgari_ustu)

def salary_increase (maas, zam_yuzdesi):
    return maas*(zam_yuzdesi+100)/100

maas_Degisimi = {}

for i in range((len(maaslar))):
    if  maaslar[i]>50:
        break          #break döngüyü kapatır sonraki döngüye geçer. Continue ise atlatır
    elif maaslar[i]<30:
        maas_orani=30
    else:
        maas_orani=10
    maas_Degisimi[maaslar[i]]=salary_increase(maaslar[i], maas_orani)
    maaslar[i]=salary_increase(maaslar[i], maas_orani)
   
print(maaslar)
print(maas_Degisimi)

sayi = 0

while sayi <10:
    sayi+=2
    print(sayi)
    
# break and continue difference easiest example

sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        break
    print(i)
    

for i in sayilar:
    if i == 30:
        continue
    print(i)
        

    