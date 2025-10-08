# list kosong
list_kosong =[]
# list yang berisi kumpulan string 
list_buah =['Pisang', 'Nanas', 'Melon', 'Durian']
# list yang berisi kumpulan integer
list_nilai =[80,70,90,60]
# list campuran
list_jawaban =[150,33.33, 'Presiden suekarno', False]
print('list_kosong:', list_kosong)
print('list_buah:', list_buah)
print('list_nilai:', list_nilai)
print('list_jawaban:', list_jawaban)
print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])
#ubah data pertama
list_buah[0]='Jeruk'
#ubah data terakhir
list_buah[-1]='mangga'
print(list_buah)
#ubah data dalam range
list_buah[1:3]=['naga','pepeya']
print(list_buah)
#tambah data di belakang list
list_buah.append('sirsak')
print(list_buah)
#tambah data index mana pun dalam list
list_buah.insert(2,'manggis')
print(list_buah)
list_angka=[1,2,3,4,5,]
print(list_angka)
#hapus satu angka di belakang
angka_yang_terhapus=list_angka,pop()
print('angka yang terhapus:',angka_yang_terhapus)
print(list_angka)
#hapus item pertamadengan nilai 'jambu'
list_buah.remove('jambu')
print(list_buah)
