#typedproperty.py
#
#Exercise 7.7

from os import name


def Typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop

String = lambda name : Typedproperty(name, str)
Integer = lambda name : Typedproperty(name, int)
Float = lambda name : Typedproperty(name, float)