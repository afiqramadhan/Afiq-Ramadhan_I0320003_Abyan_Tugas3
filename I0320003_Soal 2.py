#Membuat Dictionary Sesuai Soal
dict = {'Name':'Afiq Ramadhan',
        'Hobi': 'Main game, Membaca, Menulis',
        'Sosial_Media': {
            'Ig' : '@afiq_ramdhan',
            'WA' : '08123456789',
            'Telegram' : '@afiqr_me'},
        'Song' : 'Rex Orange Country-Best Friend, Adele-Rolling In The Deep, Keshi-Skeletons',
        'Food' : 'Siomay, Selat, Bakso'}
print("Namaku", dict['Name'])
print("Aku punya hobi", dict['Hobi'])
print("Kalian bisa kenal denganku lebih dekat di", dict['Sosial_Media'])
print("Musik favoritku adalah", dict['Song'])
print("Makanan kesukaanku adalah", dict['Food'])

#Update Dictionary
dict = {'Name':'Afiq Ramadhan',
        'Hobi': 'Main game, Membaca, Menulis',
        'Sosial_Media': {
            'Ig' : '@afiq_ramdhan',
            'WA' : '08123456789',
            'Telegram' : '@afiqr_me'},
        'Song' : 'Rex Orange Country-Best Friend, Adele-Rolling In The Deep, Keshi-Skeletons',
        'Food' : 'Siomay, Selat, Bakso'}
dict['Hobi'] = 'Main game, Menonton Film, Menulis'
dict['Sosial_Media'] = 'Ig: @afiq_ramdhan, WA: 08123456789, Line: @ramadhan'
del dict['Food']

