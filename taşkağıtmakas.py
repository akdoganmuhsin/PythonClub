import random as rd
tkm= ("taş","kağıt","makas")
b_score=0
a_score=0
while a_score<3 and b_score<3:
    a=str(input("Taş,kağıt,makas seçeneklerinden birini seçiniz:"))
    b=str(rd.choice(tkm))
    if  a=="taş":
        if b=="taş":
            print("berabere",a_score,b_score)
        elif b=="makas":
            a_score+=1
            print("insan kazanır",a_score,b_score)
        elif b=="kağıt":
            b_score+=1
            print("bilgisayar kazanır",a_score,b_score)

    elif a=="makas":
        if b=="taş":
            b_score+=1
            print("bilgisayar kazanır",a_score,b_score)
        elif b=="makas":
            print("berabere",a_score,b_score)
        elif b=="kağıt":
            a_score+=1
            print("insan kazanır",a_score,b_score)
    elif a=="kağıt":
        if b=="taş":
            a_score+=1
            print("insan kazanır",a_score,b_score)
        elif b=="makas":
            b+=1
            print("bilgisayar kazanır",a_score,b_score)
        elif b=="kağıt":
            print("berabere",a_score,b_score)

if a_score==3:
    print("tebrikler kazandınız!!,insan kazandı")
elif b_score==3:
    print("tebrikler kazandınız!!,bilgisayar kazandı")















