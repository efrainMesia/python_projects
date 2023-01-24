import importlib
from importlib import util
import inspect
import types
import functools
import os
from contextlib import contextmanager
import sys

def decorate_all_in_module(module,code_line):
    classes_only = [m[0] for m in inspect.getmembers(module, inspect.isclass) if m[1].__module__ == module.__name__]
    classes = [getattr(module,new_class) for new_class in classes_only]
    test = module()
    func_callable = []
    for class_item in classes:
        for attr, item in class_item.__dict__.items():
            if callable(item):
                    func_callable.append(attr)
                    setattr(class_item, attr,decorate_func(item,code_line))
    class_objs = [getattr(module,new_class)() for new_class in classes_only]
    for class_obj in class_objs:
        for attr in dir(class_obj):
            class_func = getattr(class_obj,attr)
            if attr in func_callable:
                class_func()
    
def decorate_func(func,line_code):
    def ret(*args):
        print(func.__name__)
        func_ret = func(*args)
        if func_ret != None:
            print(func_ret)
        exec(line_code)
    return ret

def path_import(absolute_path):
   '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
   with add_to_path(os.path.dirname(absolute_path)):
       spec = util.spec_from_file_location(absolute_path, absolute_path)
       module = util.module_from_spec(spec)
       spec.loader.exec_module(module)
       return module

@contextmanager
def add_to_path(p):
    import sys
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path

#def str_to_class(str):
#    print(f"{sys.modules} **********")
#    return getattr(sys.modules[__name__],str)


if __name__ == '__main__':
    name_file = input("Enter the python file: ")
    file_path =  os.path.dirname(name_file) 
    code_line = "print(\"hello\")"
    #name_file=name_file.replace("\\",".")
    #print(name_file)
    imported_module = path_import(name_file)
    #print(imported_module)
    #print(dir(imported_module))
    # Main code run obj
    test = decorate_all_in_module(imported_module,code_line)
