import re
def bubbleSort(arr): #Fungsi Bubble Sort
    
    if not all (isinstance(x, int) for x in arr): #cek apakah nilai dalam list integer semua
        raise ValueError ('Semua Data harus berupa angka.')
    
    panjang_Data = len(arr) #Hitung Panjang List
    
    for i in range (panjang_Data): #Looping untuk setiap putaran
        swapped = False
        
        for j in range (0, panjang_Data - i - 1): #Looping untuk membandingkan element didalam list
            
            if arr[j] > arr[j + 1]: #jika elemen yang ditemukan lebih besar dibandingkan elemen setelahnya maka tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
        if swapped == False:
            break
                
    return arr #Mengembalikan nilai arr

if __name__ == "__main__": #Run jika program dijalankan langsung
    user_input = input('Masukan beberapa angka yang ingin diurutkan: ') #fitur untuk user
    
    user_list = re.split(r'[,\s]+', user_input.strip()) #memecahkan input user menjadi list berdasarkan koma dan spaci
    
    data = [] #menampung data valid
    invalid_elements = [] #menampung data tidak valid
    # data = [12, 81, 41, 1, "dua satu", 60] #Variabel yang menampung list data
    
    for x in user_list: #memeriksa elemen pada user list
        try:
            data.append(int(x)) #coba ubah integer, jika berhasi tambahkan ke data
        except ValueError:
            invalid_elements.append(x) #jika gagal, maka masuk dalam invalid argumen
            
    if invalid_elements: #jika ada element tidak valid tampilkan pada user
        print(f"❌ Elemen berikut bukan angka dan dilewatkan: {invalid_elements}")
        
    if data: #jika data valid tampilkan data sebelum di urutkan dan sesudah
        print(f"Data valid sebelum Bubble Sort: {data}")
        print(f"Data setelah Bubble Sort: {bubbleSort(data)}")
        
    else: #jika semua data tidak valid
        print("⚠️ Tidak ada data valid untuk diurutkan.")
    