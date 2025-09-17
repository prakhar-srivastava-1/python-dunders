"""
This file looks at 3 basic dunders for object creation.
- __new__
- __init__
- __del__
- __copy__
- __deepcopy__
"""
class DunderExamples:
    """Class demonstrating use of Object lifecycle dunders"""
    
    def __new__(cls, *args, **kwargs):
        """
        This is the object constructor (not __init__)

        Good Use Case: Singleton

        Args:
            cls: class
        """
        print("Inside __new__")
        # create an object using super
        instance = super().__new__(cls)
        # set a custom_attribute
        instance.custom_attribute = "Custom Attribute in __new__" 
        return instance
    
    def __init__(self, value, *args, **kwargs):
        """
        Initialises the constructed object with values
        """
        print("Inside __init__")
        self.value = value


# Execution
dunder_obj = DunderExamples(10)
print(f"value: {dunder_obj.value}")
print(f"custom_attribute: {dunder_obj.custom_attribute}")

# Output
"""
Inside __new__
Inside __init__
value: 10
custom_attribute: Custom Attribute in __new__
"""