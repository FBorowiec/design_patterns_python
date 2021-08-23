# **Factory pattern**

## **Intent**

- Use when object creation logic becomes too convoluted
- Initializer is not descriptive
    - Name is always `__init__`
    - Cannot overload with same sets of arguments wieh different names
    - Can turn into 'optional parameter hell'
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to
    - A separate method (Factory Method)
    - That may exist in a separate class (Factory)
    - Can create hierarchy of factories with Abstract Factory

## **Description**

It is a component responsible solely for the wholesale (non-piecewise creation of objects).
