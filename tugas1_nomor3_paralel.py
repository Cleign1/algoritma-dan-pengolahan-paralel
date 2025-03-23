import multiprocessing
import time
import sys

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

def bilangan_prima_di_range(start, end):
    return [num for num in range(start, end + 1) if bilangan_prima(num)]

def temukan_prima_paralel(limit, num_processes=None):

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # Split the work into chunks
    chunk_size = (limit - 1) // num_processes + 1
    ranges = [(max(2, i * chunk_size), min(limit, (i + 1) * chunk_size - 1)) 
              for i in range(num_processes)]
    
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Map the work to the processes
        results = pool.starmap(bilangan_prima_di_range, ranges)
    
    # Combine the results from all processes
    all_primes = []
    for result in results:
        all_primes.extend(result)
    
    return sorted(all_primes)

if __name__ == "__main__":
    # Get the limit from command line argument or use default
    limit = int(input("Masukkan angka: "))
    
    # Get number of processes to use (optional)
    num_processes = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    start_time = time.time()
    primes = temukan_prima_paralel(limit, num_processes)
    end_time = time.time()
    
    print(f"Ditemukan {len(primes)} Bilangan Prima Sampai {limit}")
    print(f"Bilangan Awal Prima: {primes[:10]}...")
    print(f"Bilangan AKhir Prima: ...{primes[-10:]}")
    print(f"Waktu Eksekusi Paralel: {end_time - start_time:.4f} Detik")
    print(f"Prosesor yang digunakan: {num_processes or multiprocessing.cpu_count()}")
    
## benchmark dari program ini untuk mencari bilangan prima dari 0 sampai 10.000.000 adalah 20.9818 detik dengan 12 CPU Core pada prosesor Intel Core i7-8750h.