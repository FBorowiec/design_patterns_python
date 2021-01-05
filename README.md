# Design Patterns

This is my Design Patterns repository containing state of the art examples of practical usage of Design Patterns in Python.

## Gamma Categorization

Design Patterns are typically split into three categories. This is called _Gamma Categorization_ after Erich Gamma, one of Gang of Four authors.

1. **Creational Patterns**:
   * Deal with the creation (construction) of objects
   * Explicit (constructor) vs. implicit (DI, reflection, etc.)
   * Wholesale (single statement) vs. piecewise (step-by-step)
2. **Structural Patterns**:
   * Concerned with the structure (e.g. class members)
   * Many patterns are wrappers that mimic the underlying class' interface
3. **Behavioral Patterns**:
   * They are all different - no central theme

## How to run the code locally with *Bazel* already installed on host

### Bazel installation

[Install Bazel](https://docs.bazel.build/versions/master/install.html)

Once you have successfully installed *Bazel* you can run the code using:

```bash
bazel test //creational_patterns/factory_pattern
```

## Run the code inside a container

You can use my following Docker image to instantiate a container locally with Ubuntu and Bazel already installed:

```bash
docker run -it --rm framaxwlad/ubuntu_dev:latest
```

There you can simply clone the repository:

```bash
git clone https://github.com/FBorowiec/design_patterns.git
cd design_patterns/
```

And use a bazel command to run the program:

```bash
bazel test //structural_patterns/exercises:structural_patterns_test
```
