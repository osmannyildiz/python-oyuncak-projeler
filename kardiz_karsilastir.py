# Kardiz Karşılaştır
# Kullanıcıdan aldığı karakter dizisi çiftlerinin eşit olup olmadığını söyler.
#
# Yazan: osmannyildiz <iamosmannyildiz@gmail.com>
# Lisans: The Unlicense <unlicense.org>


def main():
    print("(çıkmak için 'q' girin)")
    while True:
        kd1 = input("1 > ")
        if kd1 == "q":
            break

        kd2 = input("2 > ")
        if kd2 == "q":
            break

        if kd1 == kd2:
            print("aynı")
        else:
            print("farklı")
        print() # bir adet boş satır yazdırır


if __name__ == "__main__":
    main()
