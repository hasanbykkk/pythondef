

def su_hesapla(kilo):
    k_hesapla=kilo  *0.03
    e_hesapla=kilo  *0.04
    cinsiyet=input("lütfen cinsiyetinizi giriniz").lower()
    if cinsiyet=="erkek":
        print("-" * 30)
        print(e_hesapla,"litre su içmelisiniz")
        print("cinsiyetiniz", cinsiyet)
        print("-" * 30)
    elif cinsiyet=="kadın":
        print("-" * 30)
        print("cinsiyetiniz",cinsiyet)
        print(k_hesapla,"litre su içmelisiniz")
        print("-" * 30)
    elif not cinsiyet:
        print("-"*30)
        print("lütfen cinsiyetinizi giriniz")
        print("-"*30)
kilo_al=int(input("lütfen kilonuzu giriniz"))

su_hesapla(kilo_al)
def yag_oran(yag):

