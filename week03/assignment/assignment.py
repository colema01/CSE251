'''
Requirements
1. Write a multithreaded program that counts the number of prime numbers 
   between 100,000,000 and 100,370,803.
2. The program should be able to use a variable amount of threads.
3. Each thread should look over an approximately equal number of numbers.
   This means that you need to devise an algorithm that can divide up the
   370,803 numbers "fairly" based on a variable number of threads. 
4. The algorithm should work for 1 to 101 threads.
5. COMMENT every line that you write yourself.
   
Questions:
1. Time to run using 1 thread = 3.56
2. Time to run using 10 threads = 3.73
3. Time to run using 50 threads = 3.69
4. Time to run using 101 threads =3.75
4. Based on your study of the GIL (see https://realpython.com/python-gil), 
   what conclusions can you draw about the similarity of the times (short answer)?
   >
   The times are similar because GIL allows only one thread to run at a time, even on multi-core CPUs. 
   This means adding more threads doesn’t make the program faster since only one thread can work on the task at any moment. 
   The slight increase in time with more threads is due to the extra effort needed to calculate.
   >
5. Is this assignment an IO Bound or CPU Bound problem (see https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)?
   >
   This is CPU Bound because it relies on heavy calculations to determine if numbers are prime. 
   The program's performance depends on how fast the CPU can handle these computations, as it spends most of its time performing mathematical operations. 
   It’s not I/O Bound since there’s minimal input or output involved.
'''

import math
import threading
import time
from cse251functions import create_signature_file

# Global count of the number of primes found
PRIME_COUNT = 0

# Global count of the numbers examined
NUMBERS_EXAMINED_COUNT = 0

# Lock for thread-safe updates to global variables
lock = threading.Lock()

def is_prime(n: int):
    """
    Determines if a number is prime using 6k+-1 optimization.
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(start, end):
    """
    Count prime numbers in the range [start, end).
    """
    global PRIME_COUNT, NUMBERS_EXAMINED_COUNT

    local_prime_count = 0
    for number in range(start, end):
        if is_prime(number):
            local_prime_count += 1

    # Update global counters using a lock
    with lock:
        PRIME_COUNT += local_prime_count
        NUMBERS_EXAMINED_COUNT += (end - start)

def main():
    # Start and end range
    start_number = 100_000_000
    range_size = 370_803
    end_number = start_number + range_size

    # Thread configurations to test
    thread_counts = [1, 10, 50, 101]

    for thread_count in thread_counts:
        # Reset global variables
        global PRIME_COUNT, NUMBERS_EXAMINED_COUNT
        PRIME_COUNT = 0
        NUMBERS_EXAMINED_COUNT = 0

        # Calculate the range each thread will process
        range_per_thread = (range_size + thread_count - 1) // thread_count

        # List to store the threads
        threads = []

        print(f"\nRunning with {thread_count} threads...")

        # Start timer
        start_time = time.perf_counter()

        # Create and start threads
        for i in range(thread_count):
            thread_start = start_number + i * range_per_thread
            thread_end = min(thread_start + range_per_thread, end_number)
            thread = threading.Thread(target=count_primes, args=(thread_start, thread_end))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Stop timer
        total_time = time.perf_counter() - start_time

        # Print results
        print(f"Threads: {thread_count}")
        print(f"Numbers processed: {NUMBERS_EXAMINED_COUNT:,}")
        print(f"Primes found: {PRIME_COUNT:,}")
        print(f"Total time: {total_time:.2f} seconds")

        # Validate results
        assert NUMBERS_EXAMINED_COUNT == 370_803, \
            f"Expected to process exactly 370,803 numbers, but processed {NUMBERS_EXAMINED_COUNT:,}"
        assert PRIME_COUNT == 20_144, \
            f"Expected to find exactly 20,144 primes, but found {PRIME_COUNT:,}"

if __name__ == '__main__':
    main()
    create_signature_file("CSE251W25")


