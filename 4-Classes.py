#Classes

# benzer özellikleri ve davranışları olan nesneler için kullanılır

# sinif ozellikleri 
class veriBilimci():
    bolum=""
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]
    
# sinif ozelliklerine erismek
veriBilimci.bolum
veriBilimci.sql    

# sinif ozelliklerini degistirmek
veriBilimci.sql="hayir"
veriBilimci.sql

# sinif orneklemesi
ali = veriBilimci()

ali.sql
ali.bildigi_diller.append("python")
ali.bildigi_diller

veli = veriBilimci()
veli.bildigi_diller
# veli python bilmemesine rağmen alide ekleyince velide de eklendi. çözüm ->

class veriBilimci2 ():
    def __init__(self):
        self.bildigi_diller = []
        self.bolum=""
        self.sql=""
        self.deneyim_yili=0
        # self orneklemleri (oluşturulan nesneleri) temsil eder. Temsilcidir
    bildigi_diller = ["r", "sql"]
    sql = "yess"
    
# =============================================================================
#     self ile başlayanlar oluşturulan nesneye atanan değerler
#     sınıf içinde yarıca tanımlananlar sınıfın kendi özellikleridir 
# =============================================================================
        
ahmet = veriBilimci2()
ahmet.bildigi_diller = "java"

mehmet = veriBilimci2()
mehmet.bildigi_diller
# bu sefer mehmette bir dil gözükmedi

veriBilimci2.bildigi_diller

mehmet.sql

class veriBilimci3 ():
    calisanlar = []
    
    def __init__(self):
        self.bildigi_diller = []
        self.bolum=""
        veriBilimci3.calisanlar.append(self)
        # her bir yeni nesne eklendiğinde bunu çalışanlar sınıfına ekleyemedim
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
# Class üzerinden metod çağırma işlemi staticmethod dekoratörü ile yapılabilir.
        
james = veriBilimci3()
james.bildigi_diller

david = veriBilimci3()
david.bildigi_diller

veriBilimci3.dil_ekle(david,"ingilizce")
david.dil_ekle("fransızca")
david.bildigi_diller.clear()

david.bildigi_diller


dir(veriBilimci3())

#print(veriBilimci3().calisanlar)

veriBilimci3.dil_ekle


#INHERITANCE

class Employees():
    def __init__(self):
        self.firstName =""
        self.lastName =""

class DataScientists(Employees):
    def __init__(self):
        self.programmingLanguages = []
        
emin = DataScientists()
emin.firstName = "emin as expected xd"

emin.firstName


#şu ana kadar class nesnelerini hep manuel tanımladık. fonskiyonel yapmak ->

class MarketingTeam ():
    def __init__(self, storyteling, experience):
        self.storyteling = storyteling
        self.experience = experience
        if not isinstance(experience, (int, float)):
            raise ValueError("experience_in_field sadece SAYISAL bir değer olabilir.")
        
marvel = MarketingTeam("great", "ankara")
marvel.experience
marvel.experience = 55555
marvel.storyteling
        