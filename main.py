def bubbleSort(arr): #Fungsi Bubble Sort
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
    data = [12, 81, 41, 1, 21, 60] #Variabel yang menampung list data
    print(f'Data sebelum diurutkan: {data}') #Menampilkan data sebelum di urutkan
    
    print(f'Data setelah dilakukan Bubble Sort {bubbleSort(data)}') #Menampilkan data setelah diurutkan