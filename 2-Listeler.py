#Veri Yapıları

list = [20,"30",40,50]
type(list[1])
type(list[2])

list_of_lists = [12,"a",list]
#liste içine liste eklenebilir

list_of_lists[2][2]

# del list_of_lists

alt_list_on = list_of_lists[:2]
alt_liste_arka = list_of_lists[2:]


liste = ["ali","veli","ayşe","berkcan"]

liste[0:2] = "yeni_ali", "yeni_veli"

 # liste[0:2] = ["yeniler"]

liste += ["ahmet"]

liste

del liste [4:]

#liste metodları

dir(list)

# list.clear()

list.append("yeni deger")  #sona ekler

list.remove("yeni deger")  #secileni siler

list.insert(0, "0.indeks") #eleman ekledik

list.pop(0) #elemanı siler

list.insert(len(list), "son")

list.count("30")

yedek_list = list.copy()
list
list.reverse()

list.insert(1, 55)

liste_sirali = list[:4]
liste_sirali.pop(2)

liste_sirali.sort()

list.extend(list)

list.index(55)

dir(list)

#Tuple

#Tuple ın listeden tek farkı update yasak

t = ("ali","veli",3,[0,"a"])

#tek değerli olursa değerin tipi verir o yüzden sonuna bi , koymakta fayda var

t = t.__add__(t)


#listeler   -> kapsayıcı, sıralı,  değiştirilebilir
#tuplelar   -> kapsayıcı, sıralı,  DEĞİŞTİRİLEMEZ
#dictionary -> kapsayıcı, SIRASIZ, değiştirilebilir
#setler     -> kapsayıcı, sırasız, değiştirlebilir

dictionary = {"money" : [0,"to",999999],
              "school" : "okul",
              "teacher" : "hoca"}

len(dictionary)

# dictionary[0] hata atar çünkü sözlükler sırasızdır

dictionary["money"]

money=100

dict_in_dict = {money : [0,"to",999999],
              "school" : {"money" : [0,"to",999999],
                            "school" : "okul",
                            "teacher" : "hoca"},
              "teacher" : "hoca"}

dict_in_dict["school"]["money"][1]

dictionary["teacher"] = "öğretmen" #update
dictionary["new_field"] = "new value"


value = "valueee"

dictionary[value] = "value"

dictionary[list] = "liste"
#list degisebilir bir deger o yüzden bunu koyamayız. Biz keylerin sabit olduğuna güveniyoruz


#Setler (kumeler) -> sırasız, değerli unique, değiştirilebilir, hızlıdır

set(list)

newlist = [10,10,10,10,20,20,40,"ankara"]

my_set=set(newlist)
len(my_set)
set(newlist[7]) #her deger 1 kere geçer

my_set.add(12)
my_set.remove(12)

# =============================================================================
# Set ve sözlüklerin sırasız olması, performans avantajları sağlar
# Set ve sözlüklerin bu şekilde sırasız olması, çoğu durumda arama ve ekleme gibi temel işlemleri hızlandırır.
# Bu veri yapıları, birçok durumda O(1) karmaşıklığında işlemler sağlar. Ancak, bu avantaj sıralı bir yapıyla elde edilemez. O(1), sabit bir işlem süresine sahip algoritmaları ifade eder.

# =============================================================================


set1 = set([1,2,3,4])
set2 = set([1,3,5])

set1.difference(set2)  # = set1-set2
set2.difference(set1)  # = set2-set1

set1.symmetric_difference(set2)

set1.intersection(set2) # = set1 & set2

set1.union(set2)

set1.isdisjoint(set2) #kesişim kümesi boş mu?

set1.issubset(set2) #alt kümesi mi?
set1.issuperset(set2) #kapsam kümesi mi?
