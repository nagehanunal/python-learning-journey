def parola_istatistikleri(parola):
    """parolanın temel istatistiklerini hesaplar."""
    uzunluk=len(parola)
    sadece_harf_mi=parola.isalpha()
    buyuk_harf_var_mi= parola != parola.lower()
    bosluk_var_mi=" " in parola

    istatistikler={
        "uzunluk":uzunluk,
        "sadece harf mi":sadece_harf_mi,
        "buyuk harf var mı":buyuk_harf_var_mi,
        "boşluk var mı":bosluk_var_mi
    }
    return istatistikler

def parola_guc_degerlendir(parola):
    """parolanın gücünü değerlendirir."""
    puan=0

    uzunluk=len(parola)
    buyuk=[k for k in parola if k.isupper()]
    kucuk=[k for k in parola if k.islower()]
    rakam=[k for k in parola if k.isdigit()]
    ozel=[k for k in parola if not k.isalnum()]

    if uzunluk>=8:
        puan+=1
    if len(buyuk)>0 and len(kucuk)>0:
        puan+=1
    if len(rakam)>0:
        puan+=1
    if len(ozel)>0:
        puan+=1

    if puan==4:
        return "Çok Güçlü"
    elif puan==3:
        return "Güçlü"
    elif puan==2:
        return "Orta"
    elif puan==1:
        return "Zayıf"


parola=input("lütfen parolanızı giriniz:")
istatistikler=parola_istatistikleri(parola)
print(istatistikler)
guc=parola_guc_degerlendir(parola)
print("parolanızın gücü:",guc)