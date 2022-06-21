import random
import time


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durum == "Acik"):
            print("Televizyon zaten açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = "Acik"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses += 1

                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):

        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi.....")

    def rastgele_kanal(self):

        rastgele = random.randint(0, len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:", self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses,
                                                                                          self.kanal_listesi,
                                                                                          self.kanal)


kumanda = Kumanda()

while True:
    print('acmak istiyor musunuz?')
    cevap1 = input()
    cevap1.lower()
    if cevap1 == 'evet':
        kumanda.tv_ac()
    else:
        print('cikiyorsunuz')
        continue
    while True:
        print("""

Televizyon Uygulaması

1. Tv Kapat

2. Ses Ayarları

3. Kanal Ekle

4. Kanal Sayısını Öğrenme

5. Rastgele Kanala Geçme

6. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")

        işlem = input("İşlemi Seçiniz:")

        if (kumanda.tv_durum == 'Acik'):

            if (işlem == "1"):
                kumanda.tv_kapat()
                break

            elif (işlem == "2"):
                kumanda.ses_ayarları()

            elif (işlem == "3"):
                kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

                kanal_listesi = kanal_isimleri.split(",")

                for eklenecekler in kanal_listesi:
                    kumanda.kanal_ekle(eklenecekler)
            elif (işlem == "4"):

                print("Kanal Sayısı:", len(kumanda))

            elif (işlem == "5"):
                kumanda.rastgele_kanal()
            elif (işlem == "6"):
                print(kumanda)

            else:
                print("Geçersiz İşlem......")
        else:
            print('tv kapali')
