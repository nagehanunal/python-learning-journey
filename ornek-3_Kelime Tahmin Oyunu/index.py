import random

film_listesi=["titanic","avatar","spiderman","matrix"]
secilen=random.choice(film_listesi)
print(secilen)  # Bu satır sadece test amaçlıdır, gerçek oyunda gizlenmelidir.

gizli_gorunum=["_"]*len(secilen)
print(" ".join(gizli_gorunum))

while "_" in gizli_gorunum:
    tahmin=input("Bir harf tahmin edin: ").lower()

    bulundu=False
    for i in range(len(secilen)):
        if secilen[i]==tahmin:
            gizli_gorunum[i]=tahmin
            print(" ".join(gizli_gorunum))
            bulundu=True

    if not bulundu:
        print("Bu harf kelimede yok.")
        print(" ".join(gizli_gorunum))


print("\nTebrikler! Kelimeyi doğru bildiniz:", secilen)