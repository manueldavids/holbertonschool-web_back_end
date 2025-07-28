# Python - Variable Annotations

## Project Overview

This project focuses on implementing and understanding Python variable annotations, a feature introduced in Python 3.6 that allows developers to specify the expected types of variables, function parameters, and return values. The project demonstrates various aspects of type annotations including basic types, complex types, and duck typing.

## Learning Objectives

Upon completion of this project, you will be able to explain to anyone, without the help of Google:

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing principles and implementation
- How to validate code with mypy

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- The length of files will be tested using wc
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- Documentation is not a simple word, it's a real sentence explaining the purpose

## Project Structure

```
python_variable_annotations/
├── 0-add.py              # Basic addition function with type annotations
├── 1-concat.py           # String concatenation function with type annotations
├── 2-floor.py            # Floor function with type annotations
├── 3-to_str.py           # Float to string conversion with type annotations
├── 4-define_variables.py # Variable definitions with type annotations
├── 5-sum_list.py         # List of floats summation with type annotations
├── 6-sum_mixed_list.py   # Mixed list summation with Union types
├── 7-to_kv.py            # Key-value tuple creation with type annotations
├── 8-make_multiplier.py  # Function factory with Callable type annotations
├── 9-element_length.py   # Duck typing with Iterable and Sequence
└── README.md             # This file
```

## Task Descriptions

### Task 0: Basic annotations - add
**File:** `0-add.py`

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

**Key Concepts:**
- Basic type annotations for function parameters and return values
- Float arithmetic operations
- Function documentation standards

### Task 1: Basic annotations - concat
**File:** `1-concat.py`

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

**Key Concepts:**
- String type annotations
- String concatenation operations
- Type consistency in string operations

### Task 2: Basic annotations - floor
**File:** `2-floor.py`

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

**Key Concepts:**
- Math module integration
- Type conversion (float to int)
- Mathematical function implementation

### Task 3: Basic annotations - to string
**File:** `3-to_str.py`

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

**Key Concepts:**
- Type conversion annotations
- String representation of numbers
- Built-in function usage with type hints

### Task 4: Define variables
**File:** `4-define_variables.py`

Define and annotate variables with specified values:
- `a`: integer with value 1
- `pi`: float with value 3.14
- `i_understand_annotations`: boolean with value True
- `school`: string with value "Holberton"

**Key Concepts:**
- Variable type annotations
- Multiple data type declarations
- Type annotation syntax for variables

### Task 5: Complex types - list of floats
**File:** `5-sum_list.py`

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

**Key Concepts:**
- Complex type annotations using `typing.List`
- List processing with type safety
- Generic type usage

### Task 6: Complex types - mixed list
**File:** `6-sum_mixed_list.py`

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**Key Concepts:**
- Union types for mixed data types
- Type flexibility with `typing.Union`
- Handling heterogeneous collections

### Task 7: Complex types - string and int/float to tuple
**File:** `7-to_kv.py`

Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element is the string `k` and the second element is the square of the int/float `v` annotated as a float.

**Key Concepts:**
- Tuple type annotations
- Union types for parameter flexibility
- Mathematical operations with type conversion

### Task 8: Complex types - functions
**File:** `8-make_multiplier.py`

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

**Key Concepts:**
- Callable type annotations
- Function factories
- Higher-order functions with type hints

### Task 9: Let's duck type an iterable object
**File:** `9-element_length.py`

Annotate the function's parameters and return values with appropriate types:

```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

**Key Concepts:**
- Duck typing principles
- Iterable and Sequence type annotations
- Protocol-based type checking

## Type Annotation Concepts Covered

### Basic Types
- `int`: Integer type annotations
- `float`: Floating-point type annotations
- `str`: String type annotations
- `bool`: Boolean type annotations

### Complex Types from typing Module
- `List[T]`: List type with element type T
- `Tuple[T, U]`: Tuple type with specific element types
- `Union[T, U]`: Union type allowing multiple types
- `Callable[[T], U]`: Function type with parameter type T and return type U
- `Iterable[T]`: Iterable type with element type T
- `Sequence[T]`: Sequence type with element type T

### Advanced Concepts
- **Duck Typing**: Type checking based on behavior rather than explicit type
- **Generic Types**: Parameterized types that work with multiple data types
- **Type Safety**: Ensuring type consistency at development time
- **Documentation**: Self-documenting code through type annotations

## Testing and Validation

### Manual Testing
Each task includes a corresponding main file for testing:
- `0-main.py` through `9-main.py`

### Type Checking with mypy
To validate type annotations:
```bash
mypy filename.py
```

### Style Checking with pycodestyle
To ensure code style compliance:
```bash
pycodestyle filename.py
```

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 526 - Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)

## Author

This project is part of the Holberton School curriculum, focusing on advanced Python concepts and type annotations.

## License

This project is for educational purposes as part of the Holberton School curriculum.