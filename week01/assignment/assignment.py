'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

from unittest import TestCase
from cse251functions import *


# 1)

def perform_math(initial_value: int, value: int, operation: str) -> float:
    # Check if it is addition
    if operation == '+':
        return float(initial_value + value)
    # Check if it is subtraction
    elif operation == '-':
        return float(initial_value - value)
    # Check if it is multiplication
    elif operation == '*':
        return float(initial_value * value)
    # Check if it is division
    elif operation == '/':
        if value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return float(initial_value / value)
    # Check if it is floor division
    elif operation == '//':
        if value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return float(initial_value // value)
    # Check if it is exponentiation
    elif operation == '**':
        return float(initial_value ** value)
    # If operation is invalid
    else:
        raise ValueError(f"Invalid operation '{operation}'")


# #  Test addition
# print(perform_math(10, 5, '+')) 

# # test division
# print(perform_math(10, 5, '/'))
# # test divison by 0
# print(perform_math(10, 0, '/'))



# 2) 

def find_word_index(word_to_find: str, words: list) -> int:
    try:
        # Try to find the index of the word in the list
        return words.index(word_to_find)
    except ValueError:
        # If the word is not found it will return -1
        return -1
    
# words_list = ['apple', 'banana', 'cherry', 'apple', 'orange']

# # Word found in the list
# print(find_word_index('cherry', words_list))  # Output: 2

# # Word not found in the list
# print(find_word_index('grape', words_list))  # Output: -1




# 3) 

def get_value_from_dict_using_key(key: str, word_dict: dict) -> str:

#this returns the key if found
 return word_dict.get(key, "Key is not found")


# # dictionary of fruit
# word_dict = {
#     "apple": "A fruit",
#     "banana": "A yellow fruit",
#     "cherry": "A small, red fruit"
# }

# # Key exists in the dictionary
# print(get_value_from_dict_using_key("apple", word_dict))  

# # Key does not exist in the dictionary
# print(get_value_from_dict_using_key("grape", word_dict))  







# 4) 

def get_list_of_urls_from_dict(key: str, url_dict: dict) ->list:

    # returns key
    return url_dict.get(key, [])

# dictionary
# url_dict = {
#     "search": ["https://google.com", "https://bing.com"],
#     "social": ["https://facebook.com", "https://twitter.com"],
#     "news": ["https://cnn.com", "https://bbc.com"]
# }

# # Key exists in the dictionary
# print(get_list_of_urls_from_dict("social", url_dict))


# # Key does not exist in the dictionary
# print(get_list_of_urls_from_dict("shopping", url_dict))




# 5) 

def find_url(urls: list, name: str) ->str:
    for url in urls:
        # Check if the name is a substring of the current URL
        if name in url:
            return url
    # If no match is found, return a blank string
    return ""


# 6) 
def find_str_in_file(filename: str, str_to_find: str) -> bool:

#Returns true if the string is found in the file, it is false otherwise.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if str_to_find in line:
                    return True
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"Error reading the file '{filename}': {e}")

    return False




# 7) 

class MyParentClass:
    
    def __init__(self, value: int, values: list, name: str):
        
        # Initializes with a value, list, and name.
    
        self.value = value  # Stores single value
        self.values = values  # Stores list of values
        self.name = name  # Stores the name

    def get_value_using_index(self, index: int):
        
        # Get value from the list by index.
       
        try:
            return self.values[index]  # Returns the value at index
        except IndexError:
            print("Index out of range.")  # Handles invalid index
            return None

obj = MyParentClass(1, [5, 6, 7], "3")
        




# 8) 

class MyChildClass(MyParentClass):
    
    #Extends MyParentClass by adding an age attribute.
    

    def __init__(self, value: int, values: list, name: str, age: int):
        
         #Initializes with value, values, name, and age.
         # Call parent class constructor
        
        super().__init__(value, values, name)  
        
        # Store the age attribute
        self.age = age  

childObj = MyChildClass(1, [5, 6, 7], "3", 10)




# 9) 
def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable: list, str_to_add: str) -> str:
  
    lists_are_passed_by_reference_and_mutable.append(str_to_add)  # Add the string to the list
    return lists_are_passed_by_reference_and_mutable[0]  # Return the first element of the list

# 10) TODO: Provide a quick explanation of what pass-by-reference means. Also, what does mutable mean?
'''
Pass-by-reference means the function works directly with the original object, so changes made inside the function affect it outside too. Mutable objects, like lists or dictionaries, can be changed after they’re created. 
For example, adding an item to a list inside a function updates the same list outside. This is different from immutable objects, like strings, which can’t be changed after they’re created.
'''

# 11) 
def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable: str, str_to_add: str) -> str:

    return strings_are_pass_by_reference_and_immutable + str_to_add  # Combine the strings and return a new string


# 12) TODO: What does immutable mean?
'''
Immutable means an object cannot be changed after it is created. In Python, strings, tuples, and numbers are examples of immutable objects. For example, concatenating strings creates a new string instead of modifying the original. 
This ensures the original object stays unchanged, providing stability and predictability.
'''

# Don't change any of the assert lines. All asserts should pass. You should see "All tests passed!" if all assert pass.
# If an assert doesn't pass, you will see an AssertionError (see https://www.w3schools.com/python/ref_keyword_assert.asp).
# The AssertionError will show you why it didn't pass (meaning, it is not an error with the assertion code, but with your code)

def main():
    ''' Know how to:
        - Call a function
        - Pass in parameters to a function in the correct order
        - Use correct parameter data types
        - Return a value from a function
        - Return correct data type from a function
        - Return from all call paths in a a function
        - Write an IF statement
        - Reading: https://www.geeksforgeeks.org/python-functions/
    '''
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    ''' Know how to:
        - Use a list
        - Use the index function on a list
        - Reading: https://www.geeksforgeeks.org/python-lists/
    '''
    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    ''' Know how to:
        - Use a dictionary
        - Use a key to get the value in a dictionary
        - Understand that a dictionary value can be list
        - Know how to get the list using a key
        - Know how to write a FOR loop
        - Know how to use "in" keyword
        - Reading: https://www.geeksforgeeks.org/python-dictionary/
    '''
    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10
    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films":
                  ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    '''
        - Know how to make a Python Class
        - Know how to write a constructor
        - Know how to make attributes in a constructor
        - Understand how to use "self" in Python
        - Know how to instantiate an object of a class (shown below)
        - Know how to obtain the value using the object's attribute (shown below)
        - Know what a method is and how to write one
        - Know how to return a value from a method
        - Know to obtain a value at a specific index in a list
        - Know how to extend a class
        - Understand that an extended/child class inherits everything from parent class
        - Readings: https://www.geeksforgeeks.org/python-classes-and-objects/, https://www.geeksforgeeks.org/extend-class-method-in-python/, https://realpython.com/python-super/
    '''
    # 13) TODO instantiate an object using MyParentClass with the following three parameters: (1, [5, 6, 7], "3")
    obj = MyParentClass(1, [5, 6, 7], "3")
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7

    # 14) TODO instantiate an object using MyChildClass with the following four parameters: (1, [5, 6, 7], "3", 10).
    # 15) TODO: do NOT duplicate the code in the parent class when writing the child class. For example, the parent
    # class constructor already creates the value, values, and name parameters. Do not write these in the child
    # class. Instead, the child constructor should call the parent constructor. Same for the 'get_value_using_index'
    # function, do not rewrite this in the child class.
    childObj = MyChildClass(1, [5, 6, 7], "3", 10)
    assert childObj.value == 1
    assert childObj.values == [5, 6, 7]
    assert childObj.name == "3"
    assert childObj.age == 10
    assert childObj.get_value_using_index(0) == 5
    assert childObj.get_value_using_index(1) == 6
    assert childObj.get_value_using_index(2) == 7
    assert isinstance(childObj, MyParentClass) == True

    '''
        - Know how to open a file
        - Know how to read lines from a file
        - Understand how to compare strings
        - Readings: https://www.geeksforgeeks.org/open-a-file-in-python/, https://www.geeksforgeeks.org/with-statement-in-python/
    '''
    assert find_str_in_file(r"C:\Users\mitch\CSE251\week01\assignment\data.txt", "g") == True
    assert find_str_in_file(r"C:\Users\mitch\CSE251\week01\assignment\data.txt", "1") == False

    '''
        - Know the difference between pass-by-reference and pass-by-value.
        - Reading: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference (read the first answer)
        - Technically python is pass-by-object-reference, if you are intested in the difference, read https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
    '''
    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"
    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(
        s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")


if __name__ == '__main__':
    main()
    create_signature_file("CSE251W25")
 