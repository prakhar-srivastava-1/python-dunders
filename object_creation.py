"""
This file looks at 3 basic dunders for object creation.
- __new__
- __init__
- __del__
- __copy__
- __deepcopy__
"""
import copy

class DunderExamples:
    """Class demonstrating use of Object lifecycle dunders"""
    
    def __new__(cls, *args, **kwargs):
        """
        This is the object constructor (not __init__)

        Good Use Case: Singleton, immutable objects

        Args:
            cls: class

        Returns:
            DunderExamples class object 
        """
        print("Inside __new__")
        # create an object using super
        instance = super().__new__(cls)
        # set a custom_attribute
        instance.custom_attribute = "Custom Attribute in __new__" 
        return instance
    
    def __init__(self, value, nums, *args, **kwargs):
        """
        Initialises the constructed object with values

        Args:
            value (int)
            nums (list[int])
        """
        print("Inside __init__")
        self.value = value
        self.nums = nums

    def __del__(self, *args, **kwargs):
        """
        Destructor to remove object (runs before garbage collection)
        """
        print("Inside __del__")

    def __copy__(self):
        """
        Copies the object however, internal objects are shared

        Returns:
            DunderExamples class object 
        """
        print("Inside __copy__")
        return DunderExamples(self.value, self.nums)
    
    def __deepcopy__(self, memo):
        """
        Copies the object with new reference
        Better to use deepcopy directly

        Args:
            memo (dict): used internally to track copied
            objects and handle circular references
        
        Returns:
            DunderExamples class object 
        """
        print("Inside __deepcopy__")
        new_nums = copy.deepcopy(self.nums)
        return DunderExamples(self.value, new_nums)


# Execution
print(f"=========== Original Object ===========")
dunder_obj = DunderExamples(10, [20, 30])
print(f"value: {dunder_obj.value}")
print(f"nums: {dunder_obj.nums}")
print(f"custom_attribute: {dunder_obj.custom_attribute}")

# deepcopy object
print(f"=========== Deepcopy Begins ===========")
dunder_obj_deepcopy = copy.deepcopy(dunder_obj)
dunder_obj_deepcopy.nums.append(100)
print(f"deepcopy object value: {dunder_obj_deepcopy.value}")
print(f"deepcopy object nums: {dunder_obj_deepcopy.nums}")
print(f"original object nums: {dunder_obj.nums}")
print(f"deepcopy custom_attribute: {dunder_obj_deepcopy.custom_attribute}")
print(f"Are deepcopy and original objects same? {dunder_obj is dunder_obj_deepcopy}")
print(f"Are deepcopy and original objects' lists same? {dunder_obj.nums is dunder_obj_deepcopy.nums}")

# copy object
print(f"=========== Copy Begins ===========")
dunder_obj_copy = copy.copy(dunder_obj)
dunder_obj_copy.nums.append(40)
print(f"copy object value: {dunder_obj_copy.value}")
print(f"copy object nums: {dunder_obj_copy.nums}")
print(f"original object nums: {dunder_obj.nums}")
print(f"copy custom_attribute: {dunder_obj_copy.custom_attribute}")
print(f"Are copy and original objects' lists same? {dunder_obj.nums is dunder_obj_copy.nums}")



# Output
"""
=========== Original Object ===========
Inside __new__
Inside __init__
value: 10
nums: [20, 30]
custom_attribute: Custom Attribute in __new__
=========== Deepcopy Begins ===========
Inside __deepcopy__
Inside __new__
Inside __init__
deepcopy object value: 10
deepcopy object nums: [20, 30, 100]
original object nums: [20, 30]
deepcopy custom_attribute: Custom Attribute in __new__
=========== Copy Begins ===========
Inside __copy__
Inside __new__
Inside __init__
copy object value: 10
copy object nums: [20, 30, 40]
original object nums: [20, 30, 40]
copy custom_attribute: Custom Attribute in __new__
Inside __del__
Inside __del__
Inside __del__
"""