
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





class MyChildClass(MyParentClass):
    
    #Extends MyParentClass by adding an age attribute.
    

    def __init__(self, value: int, values: list, name: str, age: int):
        
         #Initializes with value, values, name, and age.
         # Call parent class constructor
        
        super().__init__(value, values, name)  
        
        # Store the age attribute
        self.age = age  

childObj = MyChildClass(1, [5, 6, 7], "3", 10)