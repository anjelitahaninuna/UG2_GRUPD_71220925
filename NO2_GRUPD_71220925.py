nomor= input("Masukkan Nomor Telepon:")

if nomor[0:5]=="0816":
    print("anda merupakan operator Indosat")
    
elif nomor[0:5]=="0814":
    print("Anda menggunakan operator Telkomsel")

else:
    print("Operator anda tidak diketahui")
    