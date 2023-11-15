# l1: create classes dynamically
def dynamic_class_using_type(class_name="A"):
    parent_classes = ()    
    def print_func():
        print("self.value")
        
    namespace = {
        'value': 1,
        'print_value': print_func
    }
    namespace = type.__prepare__(class_name, parent_classes)
    return type(class_name, parent_classes, namespace)
obj = dynamic_class_using_type('AB')
print(obj.__dict__)
print(obj.print_value())


# l1: create classes dynamically, better version
def dynamic_class_using_type(class_name="A"):
    parent_classes = ()    
    namespace = type.__prepare__(class_name, parent_classes)
    
    body = """
    value = 3
    
    def print_value(self):
        print(self.value)
        
    """
    exec(body, globals(), namespace)
    return type(class_name, parent_classes, namespace)
obj = dynamic_class_using_type('AB')
print(obj.__dict__)
print(obj.print_value())


# l2: implementation of private variables in a class is basically using metaclass
class Ab:
    def __init__(self):
        self.__private_var = 3

obj = Ab()
print(obj.__dict__)  # {'_Ab__private_var': 3}
# var dict is being modified using metaclass & descriptor, same we can use function overloading


# l3: let's try implement this function overloading

