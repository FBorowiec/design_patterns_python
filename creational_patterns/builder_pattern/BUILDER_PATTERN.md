# **Builder pattern**

## **Intent**

Separate the construction of a complex object from its representation so that the same construction process can create different representations.

Some objects are simple and can be created in a single constructor call. Other objects require a lot of ceremony to create. Having an object with (e.g.) 10 constructor arguments is not productive. Instead, opt for piecewise construction. The Builder pattern provides an API for constructing an object step-by-step.

## **Applicability**

Use the Builder pattern when:

- the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
- the construction process must allow different representations for the object that's constructed.

## **Related Patterns**

Abstract Factory is similar to Builder in that it too may construct complex objects. The primary difference is that the Builder patterns focuses on constructing a complex object step by step. Abstract Factory's emphasis is on families of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory pattern is concerned, the product gets returned immediately.
A Composite is what the builder often builds.
