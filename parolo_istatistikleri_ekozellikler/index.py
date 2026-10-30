class parola_istatistikleri:
    def __init__(self, parola):
        self.parola = parola

    def istatistikler(self):
        """parolanın temel istatistiklerini hesaplar."""
        return {
            "uzunluk": len(self.parola),
            "sadece_harf_mi": self.parola.isalpha(),
            "buyuk_harf_var_mi": self.parola == self.parola.upper(),
            "bosluk_var_mi": " " in self.parola,
        }    

    def eksik_karakterler(self):
        """parolada eksik olan karakter türlerini belirler."""
        eksik = []
        if not any(k for k in self.parola if k.isupper()):
            eksik.append("büyük harf")
        if not any(k for k in self.parola if k.islower()):
            eksik.append("küçük harf")
        if not any(k for k in self.parola if k.isdigit()):
            eksik.append("rakam")
        if not any(k for k in self.parola if not k.isalnum()):
            eksik.append("özel karakter")
        return eksik

    def parola_guc_hesaplama(self):
        """parolanın gücünü hesaplar."""

        uzunluk=len(self.parola)
        buyuk=[k for k in self.parola if k.isupper()]
        kucuk=[k for k in self.parola if k.islower()]
        rakam=[k for k in self.parola if k.isdigit()]
        ozel=[k for k in self.parola if not k.isalnum()]
        bosluk=[k for k in self.parola if k.isspace()]
    
        guc = 0
        if uzunluk >= 8:
            guc += 1
        if buyuk:
            guc += 1
        if kucuk:
            guc += 1
        if rakam:
            guc += 1
        if ozel:
            guc += 1
        if bosluk:
            guc -= 1    

        if guc <= 2:
            return "Zayıf"
        elif guc == 3:
            return "Orta"
        elif guc == 4:
            return "Güçlü"  
        

class kurumsal_parola_olcer():
    def __init__(self,parola):
        super().__init__(parola)
    def parola_guc_hesaplama(self):
        """kurumsal parola gücünü hesaplar."""
        guc=0
        if len(self.parola) < 12:
            return "Zayıf (Kurumsal: Uzunluk 12'den kısa)"
        ozel_kaarakter_var=any(k for k in self.parola if k.isalnum())    
        if not ozel_kaarakter_var:
            return "Zayıf (Kurumsal: Özel karakter zorunlu)"

        return super().parola_guc_hesaplama()

            


sifre=input("şifreyi girin:")
nesne=parola_istatistikleri(sifre)
print("Parola istatistikleri:", nesne.istatistikler())  
print("Eksik karakterler:", nesne.eksik_karakterler())
print("Parola Gücü:",nesne.parola_guc_hesaplama() )
print("Kurumsal Parola Gücü:", nesne.parola_guc_hesaplama())