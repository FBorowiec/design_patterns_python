# **Prototype pattern**

When it's easier to copy an existing object to fully initialize a new one:

* To implement a prototype, partially construct an object and store it somewhere
* Deep copy the prototype
* Customize the resulting instance
* A factory provides a convenient API to using the prototype

## **Intent**

* Complicated objects (e.g., cars) aren't designed from scratch
    * They reiterate existing designs
* An existing (partially or fully constructed) design is a Prototype
* We make a copy (clone) the prototype and customize it
    * Requires 'deep copy' support
* We make the cloning convenient (e.g., via a Factory)

## **Description**

A *prototype* is a partially or fully initialized object that you copy (clone) and make use of.
