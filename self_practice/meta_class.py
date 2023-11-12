def dynamic_class_using_type(class_name="A"):
    parent_classes = ()
    
    def print_func():
        print("self.value")
        
    dict_attributes = {
        'value': 1,
        'print_value': print_func
    }
    return type(class_name, parent_classes, dict_attributes)


class CustomMeta(type):
    pass

obj = dynamic_class_using_type('AB')
print(obj.__dict__)
print(obj.print_value())