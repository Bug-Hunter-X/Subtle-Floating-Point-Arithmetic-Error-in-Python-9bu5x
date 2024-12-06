# Subtle Floating-Point Arithmetic Error in Python

This repository showcases a common yet often overlooked error related to floating-point arithmetic and exception handling in Python. The `bug.py` file contains code that demonstrates how near-zero inputs can lead to unexpected results or exceptions.

The `bugSolution.py` file presents a refined version of the code that addresses these issues, highlighting best practices for handling potential exceptions and improving the reliability of calculations involving floating-point numbers.

The core issue lies in the imprecise nature of floating-point representation and the possibility of encountering results that are 'close enough' to zero to trigger exceptions in calculations like division. The solution demonstrates how to address these issues gracefully.