#Contoh cara menghapus pada Dictionary Python
dict = {'Name': 'Dendy', 'Age': 19, 'Class': 'College'}
del dict['Name'] # hapus entri dengan key 'Name'
dict.clear() # hapus semua entri di dict
del dict # hapus dictionary yang sudah ada

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])