#Buatlah sebuah program list (gunakan kaidah pemograman list) untuk menyimpan
#nama teman-mu:
#- isi list sebanyak 10
#- Tampilkanlah isi list indeks nomor 4,6,7.
#- Gantilah nama teman mu yang berada di list 3,5,9
#- Tambahkanlah 2 nama teman mu
#- Tampilkan semua teman kamu dengan perulangan
#- Tampilkan panjang list

list = ['Adhi','Agus','Rafi','Anisa','Athalla','Dani','Dhea','Erika','Fajri','Vizal']
print ("Menampilkan isi list indeks nomor 4,6,7 :", list[4],list[6],list[7])
list[3] = 'Bagus'
list[5] = 'Candrika'
list[9] = 'Rian'
list.append('Ayu')
list.append('Zaky')
list.sort();
print("Menampilkan semua nama dengan perulangan")
for perulangan in list:
    print(perulangan)
print("Panjang list yang ada =",len(list))
