

tel_rehber=dict()

def kişiekle(x):
    print(" *kişi ekleme ekranına hoşgeldiniz*")
    isim=input("numarasını ekliyceğiniz kişinin ismi")
    numara=input("ekleyeceğiniz kişinin numarası ")
    x=tel_rehber.setdefault(isim,numara)


def kişigöster(x):

    print(" *rehbere hoşgeldiniz*")
    kişisayısı = len(x)
    print("rehberinizdeki kişi sayısı", kişisayısı)
    for i,j in x.items():
        print(i,"",j)

def numarasil(x):
    print(" *kişi silme ekranına hoşgeldiniz*")
    silinecekkişi=input("silinecek kişiyi yazınız")
    x=tel_rehber.pop(silinecekkişi)

while True:
    işlem=int(input("yapacagınız işlemi seçin 1-numara ekle ,2-numara göster,3-numaraları sil"))
    if işlem==1:
        kişiekle(tel_rehber)
    elif işlem==2:
        kişigöster(tel_rehber)
    elif işlem==3:
        numarasil(tel_rehber)
    else:
        print("lütfen istenen tuşlara basınız")




