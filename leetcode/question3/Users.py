

class Users():
    def __init__(self,name, profession):
        self.name = name
        self.profession = profession



class Engineer(Users):
    def __init__(self,name, profession):
        super().__init__(name,profession)


class Technician(Users):
    def __init__(self,name, profession):
        super().__init__(name,profession)

class Barber(Users):
    def __init__(self,name, profession):
        super().__init__(name,profession)


class Politician(Users):
    def __init__(self,name, profession):
        super().__init__(name,profession)

class Eletrical(Engineer):
    def __init__(self,name, profession):
        super().__init__(name,profession)

class Computers(Engineer):
    def __init__(self,name, profession):
        super().__init__(name,profession)

class Machines(Engineer):
    def __init__(self,name, profession):
        super().__init__(name,profession)    

def class_creator(_new_class, _base_class, _new_method, _new_attr):
    g = globals().copy()
    attr_dict = {
                _new_method: lambda self: print("Self: " + self + " Method "),
                _new_attr: ""
                }
    parent_class =()
    for name, obj in g.items():
        if _base_class == name:
            parent_class=(obj,)

    gen_class = type(_new_class, parent_class,attr_dict)
    return gen_class

if __name__ == "__main__":
    new_class = input("Please enter the name of new class:")
    base_class = input("Please enter name of base class (blank if none):")
    new_method = input("Please enter name of new method for class Student:")
    new_attr = input("Please enter name of new attribute for class Student:")

    generate_new_class = class_creator(new_class, base_class, new_method, new_attr)
    print("Class " + new_class + " created with base class: " + base_class)
    print("Class __name__ is: " + generate_new_class.__name__)
    print("Class __dict__ is: " + str(generate_new_class.__dict__))
