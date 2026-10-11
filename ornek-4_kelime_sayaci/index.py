def say(kelime,metin):
    sayac=0
    if len(kelime)==1:
        for k in metin:
            if k==kelime:
                sayac+=1
    else:
        for i in metin.split():
            if i==kelime:
                sayac+=1
                            
    return sayac

def sesli_sessiz_harf_say(metin):
    sesli_sayac=0
    sessiz_sayac=0

    sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
   
    for i in metin:
        if i.isalpha():
            if i in sesli_harfler:
                sesli_sayac+=1
            else:
                sessiz_sayac+=1

    return sesli_sayac,sessiz_sayac            

metin=input("Metin giriniz: ").lower()
kelime=input("Kelime giriniz: ").lower()
sayac=say(kelime,metin)
print(f"{kelime} kelimesi metin içerisinde {sayac} kez geçmektedir.")
sonuc=sesli_sessiz_harf_say(metin)
print(f"Metin içerisinde {sonuc[0]} adet sesli harf ve {sonuc[1]} adet sessiz harf bulunmaktadır.")