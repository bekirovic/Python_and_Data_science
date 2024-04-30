## DONGULER

# FOR

ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)
    
# Example

maaslar=[1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    
#######################################################################
## fonksiyon ve dongu

## maaslara yuzde 20 zam yapılacak gerekli kodları yazınız

maaslar=[1000,2000,3000,4000,5000] ## maas listesini tanımla

def maas_hesabı(x): # fonksiyonla ne yapılacagını hesapla
    print(int(x*20/100+x))


for i in maaslar: # donguyle fonksiyonu dondur
    maas_hesabı(i)
    
#########################################################################

## IF,FOR,FUNC USE TOGETHER

#maası 3000 tl den dusuk olanlara yuzde 20 3000 tl den yuksek olanlara yuzde 10 zam 
maaslar=[1000,2000,3000,4000,5000]
def maas_hesabı(x):
    if x<3000:
        print(x*20/100+x)
    
    elif x>3000:
        print(x*10/100+x)
    
    else:
        print(x*15/100+x)
    
for i in maaslar:
    maas_hesabı(i)

#alternatively
def üst_maas(x):
    print(x*10/100+x)
def alt_maas(x):
    print(x*20/100+x)
def orta_maas(x):
    print(x*15/100+x)
    
for i in maaslar:
    if i<3000:
        alt_maas(i)
    elif i>3000:
        üst_maas(i)
    else:
        orta_maas(i)


        


