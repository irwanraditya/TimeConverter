##SOAL 1 - Konversi Waktu
def timeConverter(seconds): #Buat function terlebih dahulu
    hours = 0 #Variabe penampung untuk mengetahui index mana yang akan di tambahkan ke dalam output
    minute = 0 #Variabe penampung untuk mengetahui index mana yang akan di tambahkan ke dalam output
    second = seconds #Variabel untuk menjadikan parameter perhitungan dalam looping
    if second>359999 or second<0: #sebagai kondisi yang tidak dapat diterima oleh fungsi ini
        return "Invalid Input" #return yang dihasilkan apabila memasukkan parameter yang tidak sesuai
    while second > 59: #kondisi dimana detik lebih dari sebanyak 59
        minute+=1 #maka variabel menit akan bertambah sebanyak 1
        second-=60 #dan variabel detik akan berkurang sebanyak 60
    while minute >59: #kondisi dimana menit lebih dari sebanyak 59
        hours+=1 #maka variabel jam akan bertambah sebanyak 1
        minute-=60 #dan variabel menit akan berkurang sebanyak 60
    konversi = "0{}:0{}:0{}".format(hours, minute, second) #mengkonversikan bentuk dari variabel hours,minute, dan second menjadi format yang ditentukan oleh soal
    return konversi #Return hasil dari output yang didapat dari looping

seconds=int(input("Masukkan detik : ")) #untuk menginput nilai yang diinginkan untuk fungsi timeConverter
print(timeConverter(seconds)) #mencetak hasil dari fungsi timeConverter