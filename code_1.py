import time

# --- Fungsi Bubble Sort Rekursif ---
def Rekursif_Bubble(arr, n):
    """
    Mengurutkan list menggunakan Bubble Sort secara rekursif.
    """
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    Rekursif_Bubble(arr, n - 1)

# --- Fungsi Utama Program ---
def main():
    print("--- Demonstrasi List, Bubble Sort Rekursif, dan Urutan ---")

    # 1. Tipe Data List & Sequence
    # Ini adalah list (sequence) angka. Anda bisa mengubah atau menambahkannya secara manual di sini.
    my_list = [64, 34, 25, 12, 22, 11] 
    
    # --- TAMBAHKAN ANGKA ANDA DI BAWAH INI (opsional) ---
    # Contoh: my_list.append(50)
    #         my_list.append(5)
    # ---------------------------------------------------

    print(f"\nList awal tipe: {my_list}")
    if my_list:
        print(f"Elemen pertama tipe: {my_list[0]}")

    # Buat salinan untuk proses sorting
    list_to_sort = list(my_list)

    # 2. Bubble Sort dengan Rekursi
    if list_to_sort:
        print(f"\nList sebelum diurutkan: {list_to_sort}")
        
        start_time = time.time()
        Rekursif_Bubble(list_to_sort, len(list_to_sort)) # Memulai rekursi
        end_time = time.time()
        
        print(f"List setelah diurutkan: {list_to_sort}")
        print(f"Waktu eksekusi: {(end_time - start_time) * 1000:.4f} ms")
    else:
        print("\nList kosong, tidak ada yang diurutkan.")

if __name__ == "__main__":
    main()