'''
Requirements:
1. Create a class that extends the 'threading.Thread' class (see https://stackoverflow.com/questions/15526858/how-to-extend-a-class-in-python). This means that the class IS a thread. 
   Any objects instantiated using this class ARE threads.
2. Instantiate this thread class that computes the product of all numbers 
   between one and that number (exclusive)
3. COMMENT every line that you write yourself.

Things to consider:
a. How do you instantiate a class and pass in arguments (see https://realpython.com/lessons/instantiating-classes/)?
b. How do you start a thread object (see this week's reading)?
c. How will you wait until the thread is done (see this week's reading)?
d. How do you get the value an object's attribute (see https://datagy.io/python-print-objects-attributes/)?
'''

import threading
from cse251functions import create_signature_file

###############################
# DO NOT USE YOUR OWN GLOBALS #
###############################

class ProductThread(threading.Thread):
    def __init__(self, number):

        super().__init__()  # Created the parent Thread class
        self.number = number  # Store the number as an attribute
        self.product = None  # Make the product as None for the result later

    def run(self):

        self.product = 1  # Make the product = to 1
        for i in range(1, self.number):  # Loop through numbers 
            self.product *= i  # Multiply and update the product

def main():

    # Class with 5
    thread_5 = ProductThread(5)
    thread_5.start()  # Start the thread
    thread_5.join()  # Wait for the thread to finish
    assert thread_5.product == 24, f'Should = 24 but actually is {thread_5.product}'

    # Class with 10 
    thread_10 = ProductThread(10)
    thread_10.start()  # Start the thread
    thread_10.join()  # Wait for the thread to finish
    assert thread_10.product == 362880, f'Should equal = 362880 but actually {thread_10.product}'

    # Class with 15 
    thread_15 = ProductThread(15)
    thread_15.start()  # Start the thread
    thread_15.join()  # Wait for the thread to finish
    assert thread_15.product == 87178291200, f'Should = 87178291200 but actually {thread_15.product}'


if __name__ == '__main__':
    main()  
    print("DONE")  
    create_signature_file("CSE251W25")  

