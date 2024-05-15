# data-structures

This repository contains a collection of commonly used data structures implemented in Python.

## Table of Contents

- [Introduction](#introduction)
- [Data Structures](#data-structures)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Data structures are essential components in computer science and are used to store and organize data efficiently. This repository provides implementations of various data structures in Python, along with explanations of their usage and complexity analysis.

## Data Structures

The following data structures are included in this repository:

- **Stack**: Implements a stack using a list in Python.
- **Queue**: Implements a queue using a list in Python.
- **Linked List**: Implements a singly linked list in Python.
- **Graph**: Implements a graph using adjacency lists in Python.

Each data structure is implemented as a separate Python class, with methods for common operations associated with that data structure.

## Usage

To use these data structures in your Python project, you can simply copy the respective class implementation from this repository into your codebase. Alternatively, you can clone this repository and import the classes directly into your project.

Example usage of a stack:

```python
from stack import Stack

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
