class kitap:
    def __init__ (self,ad,yazar,sayfa):
        self.ad=ad;
        self.yazar=yazar;
        self.sayfa=sayfa;
    def bilgi_ver(self):
        return f"{self.ad}-{self.yazar} =>{self.sayfa} sayfa"

class kutuphane:
    def __init__ (self):
        self.kitaplar=[]

    def kitap_ekle (self,yeni_kitap):
        self.kitaplar.append(yeni_kitap)
        print("kitap başarıyla eklendi")

    def kitaplari_listele (self):
        if not self.kitaplar:
            print("Kütüphanede henüz hiç kitap yok.")
        else:
            for kitapl in self.kitaplar:
                print(kitapl.bilgi_ver())


kutuphanem=kutuphane()

ad=input("kitap adı:")
yazar=input("kitap yazarı:")
sayfa=input("kitap sayfa sayısı:")
sayfa_int=int(sayfa)

kitap1=kitap(ad,yazar,sayfa_int)

kutuphanem.kitap_ekle(kitap1)
kutuphanem.kitaplari_listele();
