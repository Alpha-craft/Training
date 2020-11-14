angka = input("angka: ")
#char = input("Karakter: ")

# for i in range(0,int(angka)):
#     if i %2 == 0: # bilangan ganjil
#         print(str(i) + char)
#     else:
#         print(str(i) + char)

if int(angka) % 2 == 0:
    print(angka,"adalah bilangan genap")
else:
    print(angka,"adalah bilangan ganjil")