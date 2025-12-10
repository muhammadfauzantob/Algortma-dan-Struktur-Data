liskota = [
'jakarta','surabaya','depok','bekasi','solo',
'jogjakarta','semarang','makasar'
]


for i, kota in enumerate (liskota):
    print (i, kota)

liskota = [
'jakarta','surabaya','depok','bekasi','solo',
'jogjakarta','semarang','makasar'
]
kotayangDicari =input ('ketik nama kota yang di cari')
for i, kota in enumerate (liskota):
    # kita ubah katanya ke lowercase agar
    # menjadi case insensitive
    if kota.lower() == kotayangDicari.lower():
        print("kota yang anda cari berada pada indeks",i)
        break
    else:
      print('maaf, kota yang anda cari tidak ada')
    