# **Adapter pattern**

Getting the interface you want from the interface you get.

## **Intent**

A construct which adapts an existing interface `X` to conform to the required interface `Y`.

- Determine the API you need
- Create a component which aggregates (has a reference to) the adaptee
- Intermediate representation can pile up: use caching and other optimizations
