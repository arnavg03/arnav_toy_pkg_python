# Welcome to arnav_toy_pkg

|        |        |
|--------|--------|
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

`arnav_toy_pkg` is a demonstration Python package created for Assignment 5. It provides utility functions, including a clean implementation of the Quick Sort algorithm.

## Get started

You can install this package into your preferred Python environment directly from TestPyPI:

    pip install -i https://test.pypi.org/simple/ arnav-toy-pkg

Alternatively, you can install it directly from the GitHub repository:

    pip install git+https://github.com/arnavg03/arnav_toy_pkg_python.git

## Usage

Here is a quick example of how to use the sorting algorithm included in the package:

    from arnav_toy_pkg.example import quick_sort

    # Create an unsorted list
    my_list = [34, 7, 23, 32, 5, 62, 32]

    # Sort the list
    sorted_list = quick_sort(my_list)

    print(sorted_list)
    # Output: [5, 7, 23, 32, 32, 34, 62]

## Copyright

- Copyright © 2026 Arnav Gupta.
- Free software distributed under the [MIT License](./LICENSE).
