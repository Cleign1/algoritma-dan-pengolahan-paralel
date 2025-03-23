# program sederhana untuk menghitung bilangan prima dari 0 sampai minimum 100, menggunakan metode sequential
import time

# fungsi untuk mengecek bilangan prima dari input n
def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    time_start = time.time()
    number =int(input("Masukkan angka: "))
    for i in range(number):
        if bilangan_prima(i):
            print(i)
            
    time_end = time.time()
    time_total = time_end - time_start
    print(f"Waktu eksekusi program adalah {time_total:.2f} detik")
    
## benchmark dari program ini untuk mencari bilangan prima dari 0 sampai 50,000 adalah 16.29 detik
## ini dilakukan dengan prosesor Intel Core i7-8750h dengan RAM 16GB menggunakan metode sequential