"""
This file looks at basic dunders for str.
- __new__
- __init__
- __del__
- __copy__
- __deepcopy__
"""
class StrDunders:
    """Class demonstrating use of Str operation dunders"""

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        """
        Reprsents the object (dev-focussed)
        """
        return self.name

    def __repr__(self):
        """
        Reprsents the object (dev-focussed)
        """
        return f"StrDunder(name=\"{self.name}\")"
    

# Execution
s = StrDunders("myDunderObject")
print("Name of StrDunder object:", str(s))
print("Dev-focussed StrDunder object:", repr(s))

# Output
"""
Name of StrDunder object: myDunderObject
Dev-focussed StrDunder object: StrDunder(name="myDunderObject")
"""