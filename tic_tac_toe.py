# Tic Tac Toe
# Komut satırında çalışan, iki kişilik basit bir oyun.
#
# Oyuncu her hamlede [1, 9] aralığında bir rakam girer.
# Bu rakamların tahtadaki karşılıkları şöyledir:
# | 1 2 3 |
# | 4 5 6 |
# | 7 8 9 |
# Oyunu bitmeden iptal etmek için 'q' girebilirsiniz.
#
# Fırat Özgül'e ve YazBel topluluğuna teşekkürler <3
#
# Yazan: osmannyildiz <iamosmannyildiz@gmail.com>
# Lisans: The Unlicense <unlicense.org>


import os, random


# İki boyutlu listelerin çalışma şekli sebebiyle
# tüm koordinatları (y,x) şeklinde kullanıyoruz
HANELER = (
    None,   # indekslerin 1'den başlaması için
    (0,0), (0,1), (0,2),
    (1,0), (1,1), (1,2),
    (2,0), (2,1), (2,2),
)
KAZANMA_ÖLÇÜTLERİ = (
    # yatay
    (HANELER[1], HANELER[2], HANELER[3]),
    (HANELER[4], HANELER[5], HANELER[6]),
    (HANELER[7], HANELER[8], HANELER[9]),
    # dikey
    (HANELER[1], HANELER[4], HANELER[7]),
    (HANELER[2], HANELER[5], HANELER[8]),
    (HANELER[3], HANELER[6], HANELER[9]),
    # çapraz
    (HANELER[1], HANELER[5], HANELER[9]),
    (HANELER[3], HANELER[5], HANELER[7])
)
BOŞ_HANE = "_"
GEÇERLİ_GİRDİLER = ("1", "2", "3", "4", "5", "6", "7" ,"8", "9")


def ekranı_temizle():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def tahtayı_yenile(tahta):
    ekranı_temizle()
    for satır in tahta:
        print("|", *satır, "|")
    print()


def kazanan_kontrol(oyuncu_haneler):
    for ölçüt in KAZANMA_ÖLÇÜTLERİ:
        kontrol = [True for hane in ölçüt if hane in oyuncu_haneler]
        if len(kontrol) == 3:
            return True # hamleleri argüman olarak gönderilen oyuncu kazandı
    return False # kazanan yok


def main():
    devam = True
    while devam:
        devam = False

        # değişkenlerin ilk değerleri
        oyun = True
        tahta = [
            [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE],
            [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE],
            [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE]
        ]
        haneler_x = []
        haneler_o = []
        hamle = 1
        r = random.randrange(0, 2)

        tahtayı_yenile(tahta)

        while oyun:
            # sıranın kimde olduğunun hesaplanması
            if hamle % 2 == 1:
                if r % 2 == 0:
                    işaret = "X"
                else:
                    işaret = "O"
            else:
                if r % 2 == 0:
                    işaret = "O"
                else:
                    işaret = "X"

            print(f"Sıra {işaret} oyuncusunda")
            girdi = input("> ")
            if girdi == "q":
                break
            elif girdi not in GEÇERLİ_GİRDİLER:
                print("Hatalı giriş!\n")
                continue

            y, x = HANELER[int(girdi)]
            if tahta[y][x] == "_":  # girilen hane boşsa
                if işaret == "X":
                    haneler_x.append((y,x))
                else:
                    haneler_o.append((y,x))
                tahta[y][x] = işaret
                tahtayı_yenile(tahta)
                hamle += 1

                # oyun sonu kontrol
                if hamle > 9:
                    print("BERABERE")
                    oyun = False
                    break
                elif hamle > 5:
                    if işaret == "X":   # son hamleyi X yapmışsa
                        kazandı = kazanan_kontrol(haneler_x)
                        if kazandı:
                            kazanan = "X"
                    else:   # son hamleyi O yapmışsa
                        kazandı = kazanan_kontrol(haneler_o)
                        if kazandı:
                            kazanan = "O"

                    if kazandı:
                        print(f"{kazanan} KAZANDI")
                        oyun = False
                        break
            else:
                print("Girilen hane dolu!\n")
                continue

        girdi = input("Tekrar oynamak istiyor musunuz? (e/h) ")
        if girdi == "e":
            devam = True

    print("Oyundan çıkılıyor...")


if __name__ == "__main__":
    main()
