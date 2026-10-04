#kullanici=input("Lütfen kullanıcı adınızı girin: ")
#print("Merhaba, " + kullanici)
#print(f"Hoş geldiniz, {kullanici}!")

#***********************************************************************************
#İNPUT İLE VERİYİ ALIRIZ 
#ALINAN VERİ STRİNG OLDUĞUNDAN TİP DEĞİŞTİRMEK İÇİN TİP DÖNÜŞTÜRME YAPILIR
#***********************************************************************************

# sayi=input("sayi giriniz")
# sayi_int=int(sayi)
# kare=sayi_int**2
# print(f"{sayi} üssü 2 = {kare}")


# ÖRNEK:1- Vücut Kitle Endeksi (VKE) Hesaplayıcı 
# ad=input("adınızı giriniz:")
# kilo=input("kilonuzu giriniz:")
# kilo_float=float(kilo)
# boy=input("boyunuzu giriniz:")
# boy_float=float(boy)


#**************************************************************************************
# if: İlk koşulu kontrol eder.
# elif (else if): İlk koşul tutmazsa diğer ihtimalleri sırayla kontrol eder.
# else: Hiçbir koşul uym neumáticos/uymuyorsa devreye girer.
# Karşılaştırma operatörleri: == (eşit mi?), != (eşit değil mi?), >, <, >=, <=
#**************************************************************************************

# ÖRNEK:1-devamı
# if boy_float > 3:
#     boy_float = boy_float / 100 # m'ye çevirme
# vke=kilo_float/(boy_float)**2

# print(f"sayın {ad} ,Vücut Kitle Enddeksiniz: {vke}")

# if vke<18.5:
#     print("zayıf")
# elif 18.5 <= vke <= 24.9:
#     print("Normal ağırlıkta")
# elif 25.0 <= vke <= 29.9:
#     print("Kilolu")
# else:
#     print("Obez")          


#**************************************************************************************
# Listeler (list): Sıralıdır, elemanları değiştirilebilir (mutable), köşeli parantez [] ile tanımlanır. Farklı veri tiplerini bir arada tutabilir.
# meyveler = ["elma", "armut", "muz"]
# Demetler (tuple): Sıralıdır ancak değiştirilemez (immutable - sabit veriler için idealdir), normal parantez () ile tanımlanır.
# koordinatlar = (41.0082, 28.9784)
# Kümeler (set): Benzersiz (unique) elemanları tutar, sırasızdır, tekrar eden verileri otomatik olarak temizler.
# benzersiz_sayilar = {1, 2, 3, 3, 4} (Çıktısı: {1, 2, 3, 4})

# Verileri değiştirecekseniz ve sıra önemliyse -> List
# Veriler sabit kalacaksa ve değişmeyecekse -> Tuple
# "Anahtar" ile "Değer" ilişkisi kuracaksanız -> Dictionary
# Tekrarlayan verilerden kurtulmak istiyorsanız -> Set
#**************************************************************************************

#list
# meyveler=["çilek","muz"]
# meyveler.append("elma")
# print(meyveler)

#sözlük
# ogrenci={
#     "ad":"nghn",
#     "bölüm":"yazılım müh"
# }
# print(ogrenci["ad"])


#ÖRNEK:2-
# dersvenot={
#     "ders1":88,
#     "ders2":92,
#     "ders3":100
# }

# ogrn=input("hangi dersin notunu görmek istiyorsunuz (ders1 ,ders2 ,ders3):")

# if ogrn in dersvenot:
#     print(f"{ogrn} dersinin notu: {dersvenot[ogrn]}")
# else:
#     print("Böyle bir ders bulunamadı.")


#**************************************************************************************
# def: Fonksiyon tanımlayacağımızı belirtir.
# return: Fonksiyonun bir sonuç üretmesini ve çağrıldığı yere geri döndürmesini sağlar.
#**************************************************************************************

#ÖRNEK:1-devam
# def vke_hesapla(kilo,boy):
#     vke=kilo/(boy)**2
#     return vke

# print(vke_hesapla(kilo_float,boy_float))


#**************************************************************************************
#try:
    # Hata çıkma ihtimali olan kodları buraya yazıyoruz
# except ValueError:
    # Kullanıcı sayı yerine metin/harf girerse burası çalışır
# except ZeroDivisionError:
    # Kullanıcı 0 girerse (sayı 0'a bölünemez) burası çalışır

#try: "Dene bakalım, hata çıkacak mı?" dediğimiz blok.
#except: "Eğer şu hata çıkarsa programı çökertme, bunun yerine şunu yap" dediğimiz kurtarma bloğu.
#**************************************************************************************

#değer dönüştürürken hata alınırsa çökmeyi engelleme
# try:
#    kilo=input("lütfen kilonuzu giriniz:")
#    kilo_float=float(kilo)
# except ValueError:
#    print("Lütfen sayısal bir değer giriniz!")


#**************************************************************************************
#self, o an hangi araba ile işlem yapıyorsak onu temsil eder. araba1 ile işlem yaparken self yerine araba1 geçer, araba2 ile işlem yaparken araba2 geçer. Tamamen "şu anki nesne" demektir.
# class Araba:
#     # Yapıcı metod: Arabayı ilk ürettiğimizde hangi özellikler zorunlu olsun?
#     def __init__(self, marka, renk):
#         self.marka = marka  # Arabanın markası
#         self.renk = renk  
#**************************************************************************************

#ÖRNEK:3-Öğrenci takip sistemi 

# class ogrenci:
#     def __init__(self,ad,bolum,gpa):
#         self.ad=ad
#         self.bolum=bolum
#         self.gpa=gpa
#     def bilgileri_goster(self):
#         return f"sayın {self.ad},{self.bolum} bölümündesiniz. GPA={self.gpa}"

# ad=input("lütfen adınızı giriniz:")
# bolum=input("lütfwn bolumunuzu giriniz:")
# gpa=float(input("lütfwn gpanızı giriniz:"))

# nesne=ogrenci(ad,bolum,gpa)        
# print(nesne.ad+" "+nesne.bolum)
# print(nesne.bilgileri_goster())