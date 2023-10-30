# <strong> Praktikum Python </strong>
>Tugas praktikum 3 Bahasa Pemrograman | Universitas Pelita Bangsa

## Latihan 1 
>![alt text](https://github.com/Gladis32/Praktikum_3/blob/main/ss/SS%20Latihan1.py.png?raw=true)
>Kode berikut merupakan contoh fitur dasar python untuk mengelola output dan format cetakan, berikut penejelasannya :
* Pada peggunaan _end_ bagian ini menunjukkan penggunaan argumen _end=''_  dalam pernyataan _print_ , yang mengganti karakter akhir baris _\n_ dengan karakter kosong, sehingga A, B, dan C dicetak dalam satu baris ABC. selanjutnya, ada beberapa pernyataan _print_ yang mencetak X, Y, dan Z dalam baris terpisah
* Penggunaan __separator__ digunakan untuk menentukan pemisah antara beberapa nilai yang akan dicetak dalam __print__.
><br>#menggunakan separator spasi</br>
>print(w, x, y, z)
><br>#menggunakan separator koma</br>
>print(w, x, y, z, sep=',')
><br>#menggunakan separator tanpa spasi</br>
>print(w, x, y, z, sep='')
><br>#menggunakan separator tanda titik dua</br>
>print(w, x, y, z, sep=':')
><br>#menggunakan separator -------</br>
>print(w, x, y, z, sep='-----')
* Penggunaan String Format untuk menggabungkan dan mengatur tampilan teks atau nilai dalam suatu string. Dapat mencetak nilai variabel atau data dengan format tertentu.
></br>#string format bagian pertama, mencetak angka dari 0 hingga 10, diikuti hasil dari 10^0 sampai 10^10. ini hanya mencetak angka secara biasa</br>
>print(0, 10**0)
>print(1, 10**1)
>print(2, 10**2)
><br>#String format bagian kedua, string formatting ini akan mengatur tampilan letak sisi(right-aligned). {0:>3} berarti angka pertama diright-align dalam kolom lebar 3 dan {1:>16} berarti angka kedua dirihgt-align dalam kolom lebar 16</br>
>print('{0:>3} {1:>16}'.format(0, 10**0))
>print('{0:>3} {1:>16}'.format(1, 10**1))
>print('{0:>3} {1:>16}'.format(2, 10**2))
 
## Latihan 2
>![alt text](https://github.com/Gladis32/Praktikum_3/blob/main/ss/ss%20Latihan2.py.png?raw=true)
><br>Konversi Nilai</br>
* Fungsi kode berikut berguna untuk mendapatkan data dari pengguna dan data disimpan dalam variabel a dan b.
><br>a=input("masukkan nilai a:")</br>
><br>b=input("masukkan nilai b:")</br>
><br>print("variable a=",a)</br>
><br>print("variable b=",b)</br>
* Kode ini berguna untuk menggabungkan nilai a dan b
>print("hasil penggabungan {} & {}= {}".format(a, b, a + b))
* Untuk mengkonversi nilai a dan b menjadi bilangan __integer__ dan akan mengubah nilai a dan b menajadi tipe data numerik yang dapat melakukan operasi matematika
><br>a=int(a)</br>
><br>b=int(b)</br>
><br>print("hasil penjumlahan {} + {}= {}".format(a, b, a + b))</br>
><br>print("hasil pembagian {} / {} = {}".format(a, b, a / b))</br>

## Tugas 3
>![alt text](https://github.com/Gladis32/Praktikum_3/blob/main/ss/ss%20Latihan3.py.png?raw=true)
<br>Membuat buat Diamond Pyramid</br>
* Loop pertama (membuat segmen atas pyramid)
  ><br>for i in range(5):</br>
  ><br>  x='* '</br>
  ><br>  x=x*i</br>
  ><br>  print(f'{x: ^10}')</br>
  
<br>loop ini berjalan dari 1 sama dengan 0 hingga 4 (range 5)</br>
<br>variable x diinisialisasi dengan string __'* '__ ,merupakan bola bintang yang dibangun dalam bentuk pyramid</br>
<br>variable x diperpanjang dengan menggandakannya sebanyak i kali, misalnya i = 2 akan menghasilkan x = '**'<br>
<br>string format {x: ^10} digunakan untuk mencetak x ditengah(center) dalam kolom 10, sehingga menciptakan ruang kosong disisi kiri dan kanan</br>

* Loop kedua (membuat segmen bawah pyramid)
><br>for i in range(5):</br>
><br>   x='* '</br>
><br>    x=x*(5-i)</br>
><br>    print(f'{x: ^10}')</br>

<br>loop ini berjalan dari i sama dengan 0 hingga 4 (range 5)</br>
<br>variable x dengan mengurangkan i dari 5, misalnya i = 2 x akan menjadi '* * *' ( karena i = 2 jadi 5-2 = 3)</br>



## Tugas Latihan 
### Membuat Luas dan Keliling Lingkaran 
>![alt text](https://github.com/Gladis32/Praktikum_3/blob/main/ss/ss%20tugas%20latihan.py.png?raw=true)
* variable r berfungsi untuk mengambik input dari pengguna dalam bentuk jari-jari lingakaran. fungsi __input__ digunakan untuk menerima masukkan pengguna, dan __float__ digunakan untuk mengkonversi input pengguna menjadi bilangan desimal. input tersebut disimpan dalam variabel r
  
* math pi = 22/7 untuk mengganti nilai konstanta phi yang didefinisikan dalam modul __math__
  
><br>r = float(input("Masukkan jari-jari lingkaran: "))</br>
><br>math.pi= 22/7</br>
><br>luas = math.pi * r * r</br>
><br>keliling = 2 * math.pi * r</br>

* kode ini mencetak hasil dari nilai luas dan keliling lingkaran
><br>print("Luas lingkaran:", luas)</br>
><br>print("Keliling lingkaran:", keliling)</br>
### Membuat Flowchart Luas dan Keliling Lingkaran
>![alt text](https://github.com/Gladis32/Praktikum_3/blob/main/ss/Flowchart%20luas%20%26%20Keliling%20lingkaran.png?raw=true)
