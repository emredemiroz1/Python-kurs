#Toplama, çıkarma , bölme, çarpma 
#özelliklerini yapan bir hesap makinesi örneği

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme hatası: Sıfıra bölme yapılamaz."

print("Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Bir işlem seçin (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == "1":
    print(f"Sonuç: {toplama(sayi1, sayi2)}")
elif secim == "2":
    print(f"Sonuç: {cikarma(sayi1, sayi2)}")
elif secim == "3":
    print(f"Sonuç: {carpma(sayi1, sayi2)}")
elif secim == "4":
    print(f"Sonuç: {bolme(sayi1, sayi2)}")
else:
    print("Geçersiz seçim.")