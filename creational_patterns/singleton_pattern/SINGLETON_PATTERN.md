# **Singleton pattern**

A component that is instantiated only once.

## **Intent**

For some components it only makes sense to have one in the system:

* Database repositories
* Object factories

E.g., the initializer call is expensive:

* We only do it once
* We provide everyone with the same instance

Want to prevent anyone creating additional copies.

Need to take care of lazy instantiation.
