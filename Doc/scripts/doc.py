"""
.. inheritance-diagram:: doc

"""

# sphinx.ext.inheritance_diagram.InheritanceDiagram


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(B):
    pass

class F(C):
    pass

def function_A():
    """
    dfd
    """
    print("Hello ~")

if __name__=='__main__':
    function_A()