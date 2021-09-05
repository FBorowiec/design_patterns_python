# **Bridge pattern**

Connecting components together through abstractions.

## **Motivation**

- Bridge prevents a 'Cartesian product' complexity explosion. Example
    - Base class ThreadScheduler
    - Can be preemptive or cooperative
    - Can run on Windows or Unix
    - End up with 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS

```bash

    BEFORE:

                        Thread Scheduler
                               ^
                               |
                   ________________________
                  |                        |
       Preemptive Scheduler      Cooperative Scheduler
        ^                ^         ^                ^
        |                |         |                |
  WindowsPTS         UnixPTS    UnixCTS         WindowsCTS

-------------------------------------------------------------------------------
    AFTER:

        ThreadScheduler    _____________________________
         -platformScheduler                            |
         |               |                             |
         |       PreemptiveThreadSchduler              v
 CooperativeThreadScheduler                     IPlatformScheduler
                                                 |              |
                                        UnixScheduler      WindowsScheduler
```

A Bridge is a mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
