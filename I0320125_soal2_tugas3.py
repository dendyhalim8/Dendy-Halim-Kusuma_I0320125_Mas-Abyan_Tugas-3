#Buatlah sebuah program dictionary (gunakan kaidah pemograman dictionary) yang
#berisi:
#- Nama, hobi (harus lebih dari 2), sosial media (harus lebih dari 2), lagu kesukaan (harus lebih dari 2), makanan favorit (harus lebih dari 2),
#- Ubah salah satu dari hobi dan sosial media kalian, hapus lah 2 makanan favorit kalian, dan tambahkan lah 1 hoby kalian

dict = {'Nama': 'Dendy Halim Kusuma',
        'Hobi 1': 'Makan',
        'Hobi 2': 'Tidur',
        'Facebook': 'Dendy Halim Kusuma',
        'Instagram': 'den.dendy_h.k',
        'Lagu Favorit 1': 'Lily',
        'Lagu Favorit 2': 'We Will Not Go Down',
        'Makanan Favorit 1': 'Fried shrimp',
        'Makanan Favorit 2': 'Tekwan'
        }
dict['Hobi 2'] = 'Belajar'
dict['Instagram'] = '@den.dendy_h.k'
del dict['Makanan Favorit 1']
del dict['Makanan Favorit 2']
dict['Hobi 3'] = 'Bermain'
print ("dict['Nama']: ", dict['Nama'])
print ("dict['Hobi 1']: ", dict['Hobi 1'])
print ("dict['Hobi 2']: ", dict['Hobi 2'])
print ("dict['Hobi 3']: ", dict['Hobi 3'])
print ("dict['Facebook']: ", dict['Facebook'])
print ("dict['Instagram']: ", dict['Instagram'])
print ("dict['Lagu Favorit 1']: ", dict['Lagu Favorit 1'])
print ("dict['Lagu Favorit 2']: ", dict['Lagu Favorit 2'])
