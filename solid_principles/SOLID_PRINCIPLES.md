# Solid principles

In object-oriented computer programming, SOLID is a mnemonic acronym for five design principles intended to make software designs more understandable, flexible and maintainable.

## **S. Single responsibility principle**

A given class should be responsible only for doing one thing and one thing only.
Or in other words a class should only have one reason to change.

Separation of concerns - diffrerent classes handling different, independent tasks/problems.

## **O. Open-close principle**

The system should be open to extensions (for example with inheritance) but closed to modifications

## **L. Liskov substitution principle**

Subtypes should be immediately substitutable for their base types.
  "If it looks like a duck and quacks like a duck but needs batteries, you probably have a wrong abstraction".

## **I. Interface segregation principle**

Do not create interface that are too large. Many client-specific interfaces are better than one general-purpose interface. *YAGNI* - You Ain't Going to Need It!

## **D. Dependency inversion principle**

   1. High-level modules should not depend on low-level modules. Both should depend on abstractions*.
   2. Abstractions should not depend on details. Details should depend on abstractions.

_*Abstractions - Interfaces or Base classes_