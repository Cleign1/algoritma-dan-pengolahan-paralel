import time
import os
from concurrent.futures import ProcessPoolExecutor

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
    with ProcessPoolExecutor() as executor:
        for i in range(number):
            if bilangan_prima(i):
                print(i)
    time_end = time.time()
    time_total = time_end - time_start
    print(f"Waktu eksekusi program adalah {time_total:.2f} detik")
    print(f"Jumlah CPU: {os.cpu_count()}")
    
    
## benchmark dari program ini untuk mencari bilangan prima dari 0 sampai 50,000 adalah 12.35 detik dengan 12 CPU Core pada prosesor Intel Core i7-8750h.