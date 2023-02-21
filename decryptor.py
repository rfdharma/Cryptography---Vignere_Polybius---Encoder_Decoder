import string

print("==========SELAMAT DATANG============")
print("Peraturan dalam menginput nilai: ")
print("1. Masukan file berbentuk Txt dengan isi seperti contoh\n kode mu: 1271836318")
print("2. Masukkan di dalam file yang berisi angka tidak terdapat huruf!")
print("=======================================")

alphabet = (list(string.ascii_lowercase))
number = [str(i) for i in range(0, 10)] #mengambil angka dari 0-9
special_char = list(string.punctuation) #mengambil special character
special_char.remove('\\') #menghilangkan special char yang tidak diperlukan
special_char.remove("'")  #mengabungkan huruf, angka, dan special character pada satu list dan disimpan dalam karakter
special_char.remove('`')
special_char.remove('|')
special_char.remove(';')
special_char.append(' ')

karakter = alphabet + number + special_char #mengabungkan huruf, angka, dan special character pada satu list dan disimpan dalam karakter
def tabel1(password):
    global karakter #menjadikan variabel karakter menjadi variabel global
    password = password.lower() #menjadikan passwoed huruf kecil
    list_password = []
    for i in password:
        if i not in list_password and i in karakter:
            list_password.append(i)

    angka = []  #membuat variabel angka dengan list_kosong
    huruf = [] #membuat variabel huruf denggan list_kosong
    special_chara = []
    for i in karakter:
        if i not in password:   #memisahkan antara angka, huruf, dan spesial karakter
            if i.isdigit():
                angka.append(i)
            elif i.isalpha():
                huruf.append(i)
            else:
                special_chara.append(i)  #memasukkan apabila i merupakan special character

    campuran = list_password + (sorted(huruf)) + sorted(angka) + list(special_chara) #menggabungkan list_password huruf yang telah diurutkan dan angka sepcial charaacter
    dict_poly = [campuran[i:i + 8] for i in range(0, len(campuran), 8)]
    return dict_poly


def decryption1(angka, password):
    df = tabel1(password) #membuat tabel dengan inputan password
    index = [int(i) for i in angka] #menjadikan tipe data integer
    hasil = ''  #membuat kata kosong pada hasil

    # for i in angka:
    #     for j in range(0, len(i), 2):
    #         for k in i[j:j+2]:
    #             index.append(int(k))
    for i in range(0, len(index), 2): #melakuak indexing pada tabel dan memasukannya ke dalam hasil
        hasil += df[index[i+1]-1][index[i]-1]
    return hasil

def keyword(text, key):
    key = list(key)   #fungsi def keyword yang bertujuan untuk menentukan panjang key
    if len(text) == len((key)):  #mendeklarasikan variabel key bertipe list untuk menampung paramater lokal key dari def
        return (key)
    elif len(text) > len(key): #Jika panjang text lebih besar dari panjang key, maka key tersebut akan diulang secara periodik
        for i in range(len(text) - len(key)):  #Melakukan perulangan for untuk i pada rentang panjang text kurang panjang key
            key.append(key[i % len(key)])  #Menambahkan variabel key bertipe list yang telah dilakukan perulangan secara periodik hingga sesuai dengan panjang text
    else:
        key = key[:len(text)]    #Jika panjang key lebih besar daripada panjang text maka akan melakukan perintah slicing pada key hingga panjang dari key sama dengan panjang dari text
    return ''.join(key)  #Mengembalikan nilai dari variabel key yang bertipe list menjadi karakter string


def decry_vig(text, key):  #Pembuatan fungsi decry_vig dengan parameter text dan key
    kunci=[] #Membuat list kosong dengan nama kunci
    for i in key: #Perulangan untuk setiap karakter dalam variabel key
        kunci.append(letters_to_index.get(i))  #Mengubah setiap indeks i dari key , yang sebelumnya dalam bentuk letters/huruf menjadi dalam bentuk index dengan memanfaatkan dictionary letters_to_index yang telah dibuat sebelumnya. Lalu setiap index diappend/ditambahkan ke list kunci.

    hasil=[]  #Pembuatan list kosong dengan nama hasil
    for i in text:   #Perulangan untuk setiap karakter dalam variabel text
        hasil.append(letters_to_index.get(i))  #Mengubah setiap indeks i dari text, yang sebelumnya dalam bentuk letters/huruf menjadi dalam bentuk index dengan memanfaatkan dictionary letters_to_index yang telah dibuat sebelumnya. Lalu setiap index diappend/ditambahkan ke list hasil.

    hasil2=[]                                                                      #Pembuatan list kosong dengan nama hasil2
    for i,y in zip(hasil,kunci):                                                   #Melakukan perulangan i,y dengan i adalah nilai dari setiap elemen dalam list hasil dan y adalah nilai dari setiap elemen dalam list kunci
        hasil2.append(i-y)                                                         #Append/menambahkan hasil dari i-y ke list hasil2

    hasil_akhir=''                                                                  #Pembuatan string kosong dengan nama hasil_akhir
    for i in hasil2:                                                                #Perulangan setiap elemen dalam list hasil2
        if i<0:                                                                     #Percabangan dengan kondisi i<0
            i += 64                                                                 #Apabila kondisi i<0 terpenuhi, maka i akan menambahkan dengan 64 dan hasilnya tersimpan sebagai nilai dari i yang baru. Hal ini untuk menghindari hasil/indeks yang negatif yang dapat membuat error.
            hasil_akhir += str(indeks_to_letters.get(i))                            # Mengubah setiap indeks i ke dalam bentuk huruf dengan memanfaatkan dictionary, indeks yang telah diubah ke bentuk huruf ini kemudian ditambahkan ke string kosong hasil_akhir.
        else:                                                                       #Apabila kondisi i<0 tidak terpenuhi,dalam kata lain i adalah bilangan positif, maka akan ke else statement
            hasil_akhir += str(indeks_to_letters.get(i))                            # Mengubah setiap indeks i ke dalam bentuk huruf dengan memanfaatkan dictionary, indeks yang telah diubah ke bentuk huruf ini kemudian ditambahkan ke string kosong hasil_akhir.



    return hasil_akhir



####KODE MENJALANKAN DEKRIPSI
while True:
    try:
        teks = input('masukkan judul txt contoh(keren.txt): ')            #melakukan input file txt
        with open(teks, "r") as myfile:
            data = myfile.read().splitlines()
        plain_text = ','.join(data)                                               #mengekstrak data dari plain_text
        kode = ''                                                                   #mendefinsikan kode dengan string kosong
        if plain_text[:8] != 'Kode Mu:' and not plain_text[8:].strip().isdigit(): # mengecek apakah plain text sesuai format
            print('Salah Format!, Bacalah kembali aturan diatas!')
            continue

        for i in plain_text.split(' '): #memisahkan yang spasi
            if i.isdigit(): #melakukan ekstrak file yang angka
                kode += f'{i}' #memasukkan angka
        break

    except:
        print('file tidak ada di dalam penyimpanan!')

while True:
    password = input('masukkan password: ')
    hasil = True
    for i in password:  #mengecek dengan melakukan looping pada password
        if i in karakter: #mengecek apakah i di dalam karakter
            hasil = True #menjadikan hasil sama dengan True
            break
        elif i not in karakter: #mengecek apakah i tidak ada di karakter
            print(f'Inputan {i} tidak valid!') #menampilkan bahwa input tidak valid
            hasil = False
            break

    if hasil == True:
        break #apabila benar maka break
    else:
        continue # apabila salah maka continue

df = tabel1(password) #membuat tabel dari password
hasil  = decryption1(kode, password) #melakukan decription dengan polybius

digit = string.digits  #mengenarete angka
letters = string.ascii_lowercase #mengenerate huruf
spesial = ' !"#$%&()*+,-./:<=>?@[]^_{}~' #mengenerate special character

letters_to_index = dict(zip(letters + digit + spesial, (range(len(letters + digit + spesial)))))
indeks_to_letters = dict(zip((range(len(letters + digit + spesial))), letters + digit + spesial))

key = keyword(hasil,password) #membuat passwird berulang
judul = input("masukkan judul penyimpanan: ")
ini = decry_vig(hasil,key) #melakukan deccry dengan vignere
akhir =''

for i in ini:
    if i == '~':
        akhir += '\n' #jika terdapat ~ diganti dengan \n
    else:
        akhir += i #jika tidak , maka ditambah huruf


#menulis txt dan menyimpannya di dir user

file1 = open(f"{judul}.txt", "w")  # write mode
file1.write(f'{akhir}')
file1.close()

print(akhir)