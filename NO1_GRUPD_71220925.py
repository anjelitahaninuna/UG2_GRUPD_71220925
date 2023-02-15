print("==================== MAKANAN ====================")
print("1. Telur Bakar          : Rp. 7.000\n2. Lele Terbang Mas Bhe  :Rp. 10.000")
print("3. Es Coklat Lempu      : Rp. 5.000\n4. Es Doger Langensari   :Rp. 13.000")

print("==================== PESANAN ====================")
menutelur= int(input("Telur bakar: "))
menulele = int(input("Lele terbang Mas Bhe :"))
menues = int(input("Es Coklat lempu:"))
menudoger = int(input("Es Doger Langensari:"))

#belajar lagi soal split
menu1 = menutelur*7000
menu2 =menulele*10000
menu3 = menues*5000
menu4 = menudoger*13000
jumlah =menu1+menu2+menu3+menu4


# totalnya
print("==================== TOTAL ====================")
total1 =print("TOTAL TELUR BAKAR X",menutelur,":Rp.",menutelur*7000)
total2= print("TOTAL LELE TERBANG X",menulele,":Rp.",menulele*10000)
total3 =print("TOTAL ES COKLAT X",menues,":Rp.",menues*5000)
total4 =print("TOTAL ES DOGER X",menudoger,":Rp.",menudoger*13000)
semua = print("Jumlah total biaya yang harus dibayar:Rp.",jumlah)


