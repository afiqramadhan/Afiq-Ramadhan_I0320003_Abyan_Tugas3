#Membuat list nama teman

list1 = ['Agung', 'Viandy', 'Jeremia', 'Aurel', 'Agatha', 'Harry', 'Peter', 'Jesica', 'Pulung', 'Haura']
print("List nama temanku: ", list1)

#Menampilkan nama teman pada list keempat, keenam, dan ketujuh
print("list[4]: ", list1[4])
print("list[6:7]: ", list1[6:8])

#Update nama teman pada indeks ketiga, kelima, dan kesembilan
print("list nama teman sebelum update: ",list1)
list_new = list1[:]
list_new[3] = "Budi"
list_new[5] = 'Rengga'
list_new[9] = 'Agus'
print("Nama baru pada indeks 3, 5, dan 9 secara berurutan adalah", list_new[3],',',list_new[5],',',list_new[9])
print("Nama teman setelah update: ", list_new)

#Menambahkan dua nama teman
list2 = ['Thomas', 'Wiliam']
list3 = list_new + list2
print('Aku memiliki 2 teman baru, teman-temanku bernama:',list3)

#Menampilkan panjang list serta menyebutkan nama teman
print("Temanku ada {} orang, yaitu:".format(len(list3)))
for list in list3:
    print(list)