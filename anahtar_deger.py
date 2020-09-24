# Anahtar Değer
# Kullanıcıdan aldığı anahtar-değer çiftlerini düzenli bir şekilde listeler.
#
# Yazan: osmannyildiz <iamosmannyildiz@gmail.com>
# Lisans: The Unlicense <unlicense.org>


def main():
    liste_formatı = " {} -> {} "
    sonuç_formatı = " - {} çift - "

    print("(eklemeyi bitirmek için 'q' girin)")
    liste = []
    i = 1
    while True:
        anahtar = input(f"Anahtar {i}: ")
        if anahtar == "q":
            break

        değer = input(f"Değer   {i}: ")
        if değer == "q":
            break

        liste.append((anahtar, değer))
        i += 1

    max_len_anahtar = max([len(x[0]) for x in liste])
    max_len_değer = max([len(x[1]) for x in liste])
    liste_uzunluk = len(liste_formatı) - 4 + max_len_anahtar + max_len_değer
    sonuç_mesajı = sonuç_formatı.format(len(liste))
    uzunluk = max(liste_uzunluk, len(sonuç_mesajı))

    print()
    print("-" * uzunluk)
    for anahtar, değer in liste:
        print(liste_formatı.format(
            anahtar.rjust(max_len_anahtar),
            değer.ljust(max_len_değer)
        ).center(uzunluk))
    print("-" * uzunluk)
    print(sonuç_mesajı.center(uzunluk))


if __name__ == "__main__":
    main()
