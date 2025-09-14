def bubbleSort (arr):
    panjangData = len(arr)
    
    for i in range (panjangData):
        
        for j in range (0, panjangData - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

if __name__ == "__main__":
    data = [12, 81, 41, 1, 21, 60]
    print(f'Data sebelum diurutkan: {data}')
    
    print(f'Data setelah dilakukan Bubble Sort {bubbleSort(data)}')