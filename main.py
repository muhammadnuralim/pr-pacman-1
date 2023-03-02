from prima import bilangan_prima
from list_orang import irisan_pengguna as ip

# daftar list nama orang dan list penggunaan barang
list_orang = ['a','b','c','d','e']
produk_1 = ['a','n','c','e']
produk_2 = ['c', 'd']
#mengambil irisan pengguna dua produk
nama = ip(list_orang, produk_1, produk_2)
print(nama)

#mencari nilai bil prima terhadap n_bilangan
list_prima = bilangan_prima(5)
print(list_prima)