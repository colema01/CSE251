'''
Requirements:
1. Write a function that takes a number and computes the product of all numbers between
   one and that number (exclusive). This will be the target of your thread.
2. Create a thread to run this function.
3. Assert that your products are correct for the given number.
4. COMMENT every line that you write yourself.
   
Things to consider:
a. What is the correct syntax for creating a thread with one argument?
   (see https://stackoverflow.com/questions/3221655/python-threading-string-arguments)
b. How do you start a thread? (see this week's reading) 
c. How will you wait until the thread is done? (see this week's reading)
d. Do threads (including the main thread) share global variables? (see https://superfastpython.com/thread-share-variables/)
e. How will you ensure that one thread doesn't change the value of
   your global while another thread is using it too? (We haven't learned about locks yet, so you
   won't be able to run your threads simultaneously)
f. How do you modify the value of a global variable (see https://stackoverflow.com/questions/10588317/python-function-global-variables)
'''
import threading
from cse251functions import *

# global variable to keeping track of the final product
PRODUCT = 0


def compute_product(number):
    
    global PRODUCT  # Declared global to modify the shared variable
    PRODUCT = 1  # I need the product to = 1 
    for i in range(1, number):  # Loop through numbers from 1 to (number - 1)
        PRODUCT *= i  # Multiply and update the product

def main():
    
    global PRODUCT  # Declare global for result

    # Test with 5 
    thread_5 = threading.Thread(target=compute_product, args=(5,))  # thread for number 5
    thread_5.start()  # Start the thread
    thread_5.join()  # Wait for the thread to finish
    assert PRODUCT == 24, f'Should = 24 {PRODUCT}'

    # Test with 10 
    thread_10 = threading.Thread(target=compute_product, args=(10,))  # thread for number 10
    thread_10.start()  # Start the thread
    thread_10.join()  # Wait for the thread to finish
    assert PRODUCT == 362880, f'Should = 362880 {PRODUCT}'

    # Test with 15 
    thread_15 = threading.Thread(target=compute_product, args=(15,))  # thread for number 15
    thread_15.start()  # Start the thread
    thread_15.join()  # Wait for the thread to finish
    assert PRODUCT == 87178291200, f' Should = 87178291200 {PRODUCT}'


if __name__ == '__main__':
    main()
    print("DONE")
    create_signature_file("CSE251W25")
