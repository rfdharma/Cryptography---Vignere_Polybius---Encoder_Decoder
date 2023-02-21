import string

def keyword(text, key):                                                         #fungsi def keyword yang bertujuan untuk menentukan panjang key
    key = list(key)                                                             #mendeklarasikan variabel key bertipe list untuk menampung paramater lokal key dari def
    if len(text) == len((key)):                                                 #Jika panjang key sama dengan panjang text maka mengembalikan nilai key
        return (key)
    else:
        for i in range(len(text) - len(key)):                                   #Jika panjang key lebih pendek daripada panjang text, maka key tersebut akan diulang secara periodik
            key.append(key[i % len(key)])                                       #Menambahkan nilai key yang telah diulang secara periodik ke dalam variabel key
    return ''.join(key)                                                         #Mengambil seluruh data pada variabel list key dengan bertipe string


def encode(text, key):                                                          # Fungsi def untuk melakukan proses enkripsi

    split_plaintext = [letters_to_index[i] for i in text]                       # Melakukan perintah perulangan for dengan list komprehensi untuk i sebagai iterasi di variabel text

    split_key = [letters_to_index[j] for j in key]                              # Melakukan perintah perulangan for dengan list komprehensi untuk j sebagai iterasi di variabel key
                                                                                # Lalu, nantinya masing-masing variabel i dan j akan di integrasi atau mengakses pada dict value dari letters_to_index
    sum = [split_plaintext[k] + split_key[k] for k in range(len(split_key))]    # Melakukan perintah perulangan for dengan list komprehensi yang akan menjumlahkan setiap anggota pada setiap indeks dari list split_plaintext dan split_key untuk k sebagai iterasi pada rentang dari jumlah anggota pada variabel split_key

    chipertext = ''                                                             # Mendeklarasikan variabel chipertext dengan menampung tipe null string yang berfungsi untuk menampung hasil dari enkripsi nantinya
    for encrypted in sum:                                                       # Melakukan proses enkripsi pada variabel sum dengan perulangan for
        while encrypted >= len(letters + digit + spesial):                      # Melakukan perulangan while dengan kondisi jika encrypted lebih panjang sama dengan dari jumlah anggota letters + digit + spesial
            encrypted -= len(letters + digit + spesial)                         #Maka encrypted akan dikurangi pada setiap perulangan dengan jumlah anggota dari letters + digit + spesial, Hal ini untuk memanjang untuk menyamakan jumlah anggota pada key dengan jumlah anggota dari plaintext
        chipertext += indeks_to_letters[encrypted]                              # Melakukan proses menampung data pada variabel chipertext dengan penampahan setiap perulangan dari variabel encrypted yang telah diintegrasikan pada dict indeks_to_letters

    return chipertext

###fungsi encryption polybius (encyrption1 dan tabel1)
def encryption1(df, teks, judul):
    angka = ''                                                                   #Membuat variabel angka dengan string kosong yang akan diisi dengan angka hasil encryption
    for i in teks:                                                               #Membuat looping pada teks yang diinput user
        for j in df:                                                             # melakukan looping pada tabel polybius akan menambahkan spasi sebagai pemisah
            for k in j:                                                          # melakukan looping pada list j
                if i == k:                                                       # jika program menemukan bahwa i sama dengan k yaitu elemen di dalam tabel, program akan memasuki kondisi tersebut
                    angka += f'{j.index(i) + 1}{df.index(j) + 1}'                # j.index(i) digunakan untuk mencari index dari i di list j lalu ditambah dengan satu, dan df.index(j)  mencari index dari list j pada list df lalu ditambah satu.

    file1 = open(f"{judul}.txt","w")                                             # program membuka file yang memiliki judul tertentu dan memasukin mode write atau tulis
    file1.write(f'Kode Mu: {angka}')                                             # program menulis angka hasil dari chiper dan dimasukkan ke dalam txt
    file1.close()                                                                # program melakukan saving pada txt.

    return angka

alphabet = (list(string.ascii_lowercase))#mengambil huruf alphabet dari A sampai Z
number = [str(i) for i in range(0, 10)]# mengambil angka dari 0-9
special_char = list(string.punctuation) # mengambil special character
special_char.remove('\\')#menghilangkan special character yang tidak diperlukan.
special_char.remove("'")
special_char.remove('`')
special_char.remove('|')
special_char.remove(';')
special_char.append((' '))

karakter = alphabet + number + special_char #menggabungkan huruf, angka, dan special character pada satu list dan disimpan dalam karakter.

def tabel1(password):
    global karakter
    password = password.lower()                                                    #menjadikan password huruf kecil
    list_password = [] #mendeklarasikan list_password yang berisi list kosong untuk dimasukkan angka unik dari password
    for i in password:
        if i not in list_password and i in karakter :  # melakukan pengkondisian apabila element yang dilooping dari password tidak berada di list_password (sudah dimasukkan) dan i merupakan karakter yang telah ditentukan
            list_password.append(i)  #menambahkan i kepada list_password

    angka = [] #membuat variabel angka dengan list kosong
    huruf = [] #membuat variabel huruf dengan list kosong
    special_chara = [] #membuat variabel special_chara dengan list kosong
    for i in karakter:
        if i not in password: #memisahkan antara angka, huruf, dan special character
            if i.isdigit():
                angka.append(i)
            elif i.isalpha():
                huruf.append(i)
            else:
                special_chara.append(i)  # memasukkan apabila i merupakan special character.

    campuran = list_password + (sorted(huruf)) + sorted(angka) + (special_chara)   #menggabungkan list_pasword dengan huruf yang telah diurutkan dan angka ,dan special chara
    dict_poly = [campuran[i:i + 8] for i in range(0, len(campuran), 8)]
    return dict_poly   #mengembalikkan nilai dict_poly

while True:                                                                     #melakukan looping pada program
    while True:
        try:                                                                    # memastikan judul berada di dalam penyimpanan user
            teks = input('masukkan judul txt contoh(keren.txt): ')              #membuat input kepada teks dengan memasukkan judul txt
            with open(teks, "r") as myfile:                                     #membuka file input user dan memasuki mode baca
                data = myfile.read().splitlines()                               #mengekstrak string pada txt dan disimpan ke dalam data
                break                                                           #melakukan break pada loop apabila file berhasil terbaca

        except:                                                                 #melakukan except apabila file tidak terdapat di directoty user
            print('file tidak ada di dalam penyimpanan!')

    password = input('masukkan password: ')                                  #meminta user memasukkan password yang dinginkan
    plain_text = '~'.join(data).lower() #mengekstrak data menjadi string
    hasil = True      #membuat variabel hasil dengan nilai True
    for i in plain_text + password:   #melakukan looping pada plain teks dan password
        if i in karakter:  #mengecek apakah i mencapai looping terakhir dan elemen terakhir merupakan bagian dari karakter atau i merupakan spasi
            hasil = False #menjadikan variabel hasil = False
        elif i not in karakter:   #percabangan apabila i tidak ada di dalam karakter
            for j in data: #perulangan untuk mengecek error yang ada di polybius
                if i in j: #jika i terdapat di baris tersebut maka akan menampilkan error element yang ingin ditampilkan dan baris mana yang error
                    print(f'ERROR: \n{j}')
                    print(f'karakter {i} tidak didukung')
                    break
                elif i in password: #jika i terdapat di d alam password maka program akan menampilkan password salah
                    print(f'Password anda salah')
                    print(f'karakter {i} tidak didukung')
                    break

            hasil = True #apabika salah hasil akan didefinisikan sebagai True
            break

    if hasil == True:
        continue #jika benar maka akan melakukan perulangan sampai menginput nilai yang benar
    else:
        break #jika inputan benar berarti hasil = False, maka keluar dari looping dan melanjutkna program selanjutnya


digit = string.digits                                                               #Mendeklarasikan variabel digit yang menampung data string 0 - 9
letters = string.ascii_lowercase                                                    #Mendeklarasikan variabel letters untuk menampung data string huruf a-z
spesial = ' !"#$%&()*+,-./:<=>?@[]^_{}~'                                            #Mendeklarasikan variabel spesial yang menampung data string dengan karakter spesial tertentu

letters_to_index = dict(zip(letters + digit + spesial, (range(len(letters + digit + spesial)))))                        #Membuat dictionary dengan key adalah huruf dan value adalah indeks huruf
indeks_to_letters = dict(zip((range(len(letters + digit + spesial))), letters + digit + spesial))                       #Membuat dictionary dengan key adalah indeks hurud dan value adalah huruf

kode3 = keyword(plain_text, password)
code = encode(plain_text, kode3)
df1 = tabel1(password)                                                              #membuat tabel dari password user
judul = input("masukkan judul penyimpanan: ")                                       #memasukkan judul penyimpanan kepada program
keren = encryption1(df1, code, judul)                                               #mengeksripsi masukkan baca.txt dan mengeluarkan file output
print('File Telah Enskripsi, Simpan Kode Mu Baik-Baik!')