class yapilacaklar:
    def __init__(self):
        self.gorevler=[]
    def gorev_ekle(self,gorev_ekle):
        self.gorevler.append(gorev_ekle)
        print("gorev eklendi")

    def gorevleri_listele(self):
        if not self.gorevler:
            print("eklenmiş görev yok")
        else:
            for sira, gorev in enumerate(self.gorevler,1):
                print(f"{sira}. {gorev}")

    def gorev_silme(self,sira_no):
        try:
            sira_no_int = int(sira_no)
            silinen = self.gorevler.pop(sira_no_int - 1)
            print(f"'{silinen}' başarıyla silindi!")
        except IndexError:
            print("Hata: Listede bu numaraya sahip bir görev yok!")

liste=yapilacaklar()            

while True:
    try:
        yapilacak = int(
            input(
                "1. Görev Ekle \n2. Görevleri Listele \n3. Görev Sil \n4. Çıkış\nSeçiminiz: "
            )
        )

        if yapilacak == 1:
            gorev_eklenecek = input("Eklemek istediğiniz görevi giriniz: ")
            liste.gorev_ekle(gorev_eklenecek)

        elif yapilacak == 2:
            liste.gorevleri_listele()

        elif yapilacak == 3:
            gorev_silinecek=input("Silmek istediğiniz görevin numarasını giriniz: ")
            liste.gorev_silme(gorev_silinecek)

        elif yapilacak == 4:
            print("Programdan çıkılıyor.")
            break  # Döngüyü sonlandırır

        else:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir sayı girin.")

    except ValueError:
        print("Hata: Lütfen menüden geçerli bir sayı seçin!")