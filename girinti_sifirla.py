# Girinti Sıfırla
# Belirtilen dosyanın tüm satırlarının başlarındaki
# boşluk karakterlerini (tab vb. dahil) kaldırır.
# Sonucu yeni bir dosyaya yazar.
#
# Yazan: osmannyildiz <iamosmannyildiz@gmail.com>
# Lisans: The Unlicense <unlicense.org>


YARDIM_METNİ = """
Kullanımı:
python girinti_sifirla.py DOSYA_İSMİ [ÇIKTI_DOSYA_İSMİ]

Belirtilen dosyanın tüm satırlarının başlarındaki boşluk karakterlerini (tab vb. dahil) kaldırır.
Sonucu yeni bir dosyaya yazar.

ÇIKTI_DOSYA_İSMİ girilmezse varsayılan olarak 'girintisiz_'+DOSYA_İSMİ alınır.

UYARI: ÇIKTI_DOSYA_İSMİ isminde bir dosya mevcutsa sormadan üzerine yazar.
"""


import sys


def main(argv):
    if len(argv) > 1:
        dosya_ismi = argv[1]
        if len(argv) > 2:
            çıktı_dosya_ismi = argv[2]
        else:
            çıktı_dosya_ismi = "girintisiz_" + dosya_ismi

        with open(dosya_ismi, encoding="utf-8") as d1:
            with open(çıktı_dosya_ismi, "w", encoding="utf-8") as d2:
                for satır in d1:
                    yeni_satır = satır.lstrip()

                    # Eğer satır sadece boşluk karakterlerinden
                    # oluşuyorsa satırın kaybolmasını engelliyoruz
                    if yeni_satır == "":
                        yeni_satır = "\n"

                    d2.write(yeni_satır)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print(YARDIM_METNİ)
    else:
        main(sys.argv)
