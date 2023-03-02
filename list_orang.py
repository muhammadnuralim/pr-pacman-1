def irisan_pengguna(list_nama, list_produk_1, list_produk_2):
    """
    mencari orang yang menggunakan dua produk

    parameter:
        list_nama (list): list nama orang
        list_produk_1 (list): list nama orang yang menggunakan produk 1
        list_produk_2 (list): list nama orang yang menggunakan produk 2

    result:
        nama (str): nama orang yang menggunakan dua produk
    """
    # Ubah list menjadi set
    nama = set(list_nama)
    produk_1 = set(list_produk_1)
    produk_2 = set(list_produk_2)

    # for name in nama.intersection(produk_1.intersection(produk_2)):
    #     return name
    name = [name for name in nama.intersection(produk_1.intersection(produk_2))]
    return name