# program sederhana untuk menghitung bilangan prima dari 0 sampai minimum 100, menggunakan metode sequential

# fungsi untuk mengecek bilangan prima dari input n
def bilangan_prima(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def limit_prima_sequential(limit):
    primes = []
    for num in range(2, limit + 1):
        if bilangan_prima(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    import time
    
    limit = int(input("Masukkan angka: "))
    
    start_time = time.time()
    primes = limit_prima_sequential(limit)
    end_time = time.time()
    
    print(f"Ditemukan {len(primes)} Bilangan Prima Sampai {limit}")
    print(f"Awal Bilangan Prima: {primes[:10]}...")
    print(f"Bilangan Prima Akhir: ...{primes[-10:]}")
    print(f"Waktu Eksekusi Sequential: {end_time - start_time:.4f} Detik")
    
## benchmark dari program ini untuk mencari bilangan prima dari 0 sampai 10.000.000 adalah 63.2983 detik
## ini dilakukan dengan prosesor Intel Core i7-8750h dengan RAM 16GB menggunakan metode sequential