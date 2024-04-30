# Karar & Kontrol yapıları

#True-False sorgulamarı

sinir=5000
sinir==400
#################################
#if / else

sinir= 50000
gelir=60000

if gelir < sinir:
    print("Gelir sinirdan kucuk")
    
else:
    print("Gelir sinirdan buyuk")
    
########################################3
#elif //// birden fazla kosul icin

sinir= 50000
gelir1=60000
gelir2=50000
gelir3=35000
if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir2 < sinir:
    print("uyari!")
else:
    print("Gelir sinira esit degildir")

##################################################
#uygulama
sinir = 50000
magaza_adi=input("magaza adi nedir?")
gelir =int( input("Gelirinizi Giriniz:"))
print(gelir)

if gelir > sinir:
    print("Tebrikler,"+ str(gelir)+ " ile "+ magaza_adi +" olarak,promosyon kazandınız") ## print(f"tebrikler {gelir} ile {magaza_adi} olarak,promosyon kazandınız!")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir:"+str(gelir))
else:
    print("Takibe devam")



